This is a small Python web application. 
I've used FLask to create two basic endpoints, / and /health.
/ -> shows a welcome message. 
/health -> returns "OK".
requirements.txt contains the packages that the app needs, i.e flask.
Docker puts our app in a container and makes it run the same way on any computer.
'Dockerfile' here is used to build the container using Docker.
The Dockerfile contains instructions telling the docker how to build the image. 
- starts a base image
- creates a main working directory called app
- copies requirements.txt (to install flask) and the actual app code

The docker then creates the image, runs python and the main file and makes the app available. 

