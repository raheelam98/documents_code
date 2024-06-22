# Commands : docker  

 Declarative (Standardization , can’t change or fix )

 Multi-compose ( multiple containers in one file)

**Checking to see if Docker is running:**

```bash
docker version
```

**Building the Image:**

```bash
docker build -f Dockerfile.dev -t my-dev-image .
```

**Check Images:**

```bash
docker images
```

**Verify the config:**

```bash
docker inspect my-dev-image
```

**Running the Container:**

https://docs.docker.com/engine/reference/run/

```bash
docker run --name cont_name -it image_name
```

**List Running Containers**

```bash
docker ps
```

**Running the Container and start a Bash shell:**

```bash
docker run -it image_name /bin/bash
```

**Opening the command line in the container:**

```bash
docker exec -it image_name bash
```

**==========================================**

 ###  build new image 
```shell
 docker compose up -d 
```
build the image and starts the container in detached mode 

Note :- -d, --detach  (Detached mode: Run containers in the background)

 ###  rebuild the image 
  ```shell
 docker compose up -d --build 
```
(recreate the image —> - - build)

### container detail 
 ```shell
 docker compose config 
```

### stop running container
```shell
 docker compose stop

 docker stop {OPTIONS} containerID/container_name
```

### restart container
  ```shell
 docker restart container_name/container_id
```


### stops and removes the container
```shell
 docker compose down
```
1. Stop all containers
2. Remove all containers
3. Remove all networks

### forcefully stop running container 
 ```shell
 docker kill containerID/container_name 

 docker kill {OPTIONS} containerID/container_name 
```

### view logs 
 ```shell
 docker-compose logs service-name
```

### view logs (real-time monitoring)
 ```shell
 docker-compose logs service-name -f
```
- f  (follow)(real-time.) (give all the command running on terminal)
  
### display container 
 ```shell
 docker compose ps 

 docker ps {OPTIONS}
```
-a flag:  shows us all the containers, stopped or running. {-a: Stands for "all"}

-l flag: shows us the latest container.

-q flag: shows only the Id of the containers. 

display : NAME ,  IMAGE,   COMMAND,  SERVICE,  CREATED , STATUS ,  PORTS
    
 ### container list 
```bash
 docker compose ls 

 docker container ls {OPTIONS}

 docker container  ls -a
```
display containers :-  NAME  - STATUS  -  CONFIG FILES
-a : all  (list of all containers, both running and stopped)

###  inspect container 
  ```shell
 docker inspect container_name/container_id
```
Docker containers will run into some errors in real time to debug the container’s errors you can use the following commands.

 ### delete the stopped container
  ```shell
 docker rm container_name/container_id

 docker rm {OPTIONS} ontainer_name/container_id

 docker rm -f ontainer_name/container_id
```
-f flag: remove the container forcefully.

-v flag: remove the volumes.

-l flag: remove the specific link mentioned.

###  connect with running container
  ```shell
 docker exec -it container_name_or_id /bin/bash

 docker exec {OPTIONS}
```
-d flag: for running the commands in the background. {-d: Stands for "detach"}

-i flag: it will keep STDIN open even when not attached.

-e flag: sets the environment variables

-it flag: (interactive) allows us to execute commands while the container is in a running state

Note:- This command only works until the container is running, after the container restarts, this command does not restart. 

Note: -it flage :  interact with the container's terminal
 (-i (interactive) and -t (allocate a pseudo-TTY))
/bin/bash: execute inside the container
 (/bin/bash starts an interactive bash shell within the container)


### build the docker images with the help of Dockerfile.
  ```shell
 docker build -t image_name:tag .
```
“dot” represents the current directory.

example :- build a new image of docker file

docker build -f Dockerfile -t image_name:1.0.0 .

### run a container from an image
  ```shell
 docker run image_name
```
container_name
  ```shell
 docker run --name container_name image_name
```
It creates a new container from the image specified and starts that container.

### pull image
  ```shell
 docker pull image_name
```
by default, it pulls the latest image, but you can also mention the version of the image.

### remove docker images
  ```shell
 docker rmi image_name/image_id

 docker rmi -f image_name/image_id
```
-f flag : stands for "force”,  used to forcefully remove the image, 
even if it's in use by containers.

### lists all the pulled images 
  ```shell
 docker images
```

### create a volume
  ```shell
 docker volume create volume_name
```

###  inspect a volume
  ```shell
 docker volume inspect volume_name
```

### delete a volume
  ```shell
 docker volume rm volume_name
```

### docker --- prune
  ```shell
 docker container prune {OPTIONS}

 docker image prune 

 docker volume prune -f
```
-f flag : force

remove all stopped containers, images and volumes 

**starts the services defined in a Docker Compose file using the specified profile:**
```bash
docker compose --profile profile_name up -d
```
-d flag : detached mode (containers will run in the background)
 
# commands use occasionally

### docker ports (port mapping)
  ```shell
 docker run -d -p <port_on_host> : <port_on_container> Container_name
```
-p :  <host_port>:<container_port>.   (Port Mapping)

-d :  detached mode (container runs in the background)

In order to access the docker container from the outside world, we have to map the port on our host( Our laptop for example), to the port on the container. This is where port mapping comes into play.

# Example ---
create and start a new container based on a specified Docker image :-
docker run -d -p  8001:8000  docker_image:0.0.0


### push image
  ```shell
 docker push image_name/image_id
```
Once you build your own customized image by using Dockerfile you need to store the image in the remote registry which is DockerHub for that you need to push your image by using the following command.

### docker Commit command
  ```shell
 docker commit container_name_or_id new_image_name:tag
```
After running the containers by using the current image you can make the updates to the containers by interacting with the containers from that containers you can create an image by using the following commands.

### summary of docker commands and options
  ```shell
 docker run --help
```

## docker - github
https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/14_docker 

The base command for the Docker CLI.
https://docs.docker.com/reference/cli/docker/ 

docker container
https://docs.docker.com/reference/cli/docker/container/ 

CLI Cheat Sheet
https://docs.docker.com/get-started/docker_cheatsheet.pdf

Docker Commands
https://www.geeksforgeeks.org/docker-instruction-commands/ 


20 Docker Commands You Need to Know
https://kinsta.com/blog/docker-commands/ 