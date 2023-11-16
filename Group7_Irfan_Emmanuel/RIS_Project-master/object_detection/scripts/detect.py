import argparse
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized


def detect(opt, save_img=False):
    source, weights, view_img, save_txt, imgsz = opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size
  
    # Initializing section
    set_logging()
    device = select_device(opt.device)
    
    #CUDA supports half precision
    half = device.type != 'cpu'  

    # Loading of the model
    # FP32 model
    model = attempt_load(weights, map_location=device) 
    
    # stride of the model
    stride = int(model.stride.max())  
    
    # checking the image size
    imgsz = check_img_size(imgsz, s=stride)  
    if half:
        # to FP16
        model.half()  

    # Classification of the second stage
    classify = False
    if classify:
        
        # initialize
        modelc = load_classifier(name='resnet101', n=2)  
        modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model']).to(device).eval()

    # Setting of Dataloader
    vid_path, vid_writer = None, None
    
    dataset = LoadImages(source, img_size=imgsz, stride=stride)

    # Obtaining names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    # Running of the inference
    if device.type != 'cpu':
        # run once
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  
    t0 = time.time()
    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        
        # uint8 to fp16/32
        img = img.half() if half else img.float()  
        
        # range 0 - 255 to 0.0 - 1.0
        img /= 255.0  
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # The Inference
        t1 = time_synchronized()
        pred = model(img, augment=opt.augment)[0]

        # Application of NMS
        pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes, agnostic=opt.agnostic_nms)
        t2 = time_synchronized()

        # Apply Classifier
        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        # Detection process
        # detections per image
        for i, det in enumerate(pred):  
            p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 1)
            
            # normalization gain 
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  
            if len(det):
                
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Results
                for *xyxy, conf, cls in reversed(det):
                    label = f'{names[int(cls)]} {conf:.2f}'
                    plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)
                    print ("detected")
        
            return im0
