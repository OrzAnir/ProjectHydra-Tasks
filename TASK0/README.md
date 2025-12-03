There are two endpoints, / and /health.
/ -> shows a welcome message. 
/health -> returns "OK".

The steps to run app using docker :  
Build the docker image : docker build -t my-python-app .    
Run the container : docker run -p 8080:8080 my-python-app  
Test: http://localhost:8080/health  
The screenshots are attached above.

