# Template: template-ros

This template provides a boilerplate repository
for developing ROS-based software in Duckietown.

**NOTE:** If you want to develop software that does not use
ROS, check out [this template](https://github.com/duckietown/template-basic).


## How to use it

### 1. Prepare the static obstacle avoidance

Following the commands below, the different nodes use for obstacle avoidance can be implemented.

1) Clone the demo repository.


`~LAPTOP $ git clone https://github.com/JoseTejedaGuzman/Duckiebot.git`

2) Go to the cloned folder

`~LAPTOP $ cd Duckiebot`

3) Build docker containers (Remember to replace `[DUCKIEBOT_NAME]` with the appropiate vehicle name

`~LAPTOP $ dts devel build -H [DUCKIEBOT_NAME].local`

4) Run the DEMO container:

`~LAPTOP $ dts devel run -R [DUCKIEBOT_NAME]`


If you create an executable script (i.e., a file with a valid shebang statement)
a launcher will be created for it. For example, the script file 
`/launchers/my-launcher.sh` will be available inside the Docker image as the binary
`dt-launcher-my-launcher`.

When launching a new container, you can simply provide `dt-launcher-my-launcher` as
command.
