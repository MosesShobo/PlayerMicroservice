# Player Microservice

## Description
A Flask-based microservice for managing player data, including RESTful endpoints for retrieving player records.

## Prerequisites
Familiarity with Flask, Python, Postman Client, and Docker Desktop installed on your machine

## Installation
1.	To get started, I created a folder for my project called playerMicroservice and current directory into the project’s directory.
2.	Next, I ran python3 --version to confirm that Python is installed on my computer correctly.
3.	Then, Installed virtualenv to create an isolated development environment for the Player microservice by running the command below:

pip3 install virtualenv

4.	I then created a virtual environment by running the following:
     virtualenv venv
  	
5.	Finally, I activated the virtual environment using the following commands based on my computer’s operating system which is Windows: 
   .\venv\Scripts\activate



## Process

I chose python for this project because I am familiar with it. I utilized the flask framework as it's quick and easy to use for developing RESTful services with JSON. I ran into issues with Docker because the Docker Desktop app on my Windows computer suddenly stopped working. I'm not sure what the issue was but I ended up having to reinstall it.

If I had more time, I would have included authentication for the service so only authorized users could access it. 
I would have also have implemented more HTTP request methods. For example, using POST to add new data to the CSV file.
I would have also implemented logging to monitor the status of the microservice




1) ## Set Up Your Project Structure:

I created a directory for my project to organize my files. I  have a main Python script, a CSV file for data storage, unit test files, and Docker-related files.

I created a new Flask app. 
Then, I created a directory called services. In this directory, I created a file that had the player microservice code called players.py. 
This directory also has the csv file. 

I created a second directory called tests. This is the test folder. I used pytest for the unit tests. In this directory, there are 
conftest.py - for setting up pytest,
 __init__.py - initialization file, and 
test_players.py - contains the unit test. 

Finally in the root directory, there are the requirements.txt - which holds the requirements necessary for the project (flask and pytest), 
DockerFile and .dockerignore. This structure helps with organization making it easier to add more service files and test files as needed. 

2) ## Read and Parse CSV Data:

I wrote code to read the data from the CSV file and store it in a suitable data structure (list of dictionaries)

3) ## Implement REST Endpoints:

I  used a Flask web framework to create the REST endpoints and defined routes for retrieving a list of all players and for retrieving a single player by their ID.

I made REST endpoints: 

/players which fetches the records of all players loaded from the csv file and  
/players/playerID which fetches a single requested player.

While implementing the REST endpoints, I used postman to quickly check that there were working as expected.

4) ## Write Unit Tests: 

I created unit tests to ensure that my core logic functions correctly. I used Python's built-in library called pytest,I made three tests that cover all the endpoints in test_players.py -  

test_get_players() tests the  /players endpoint. It checks that all the players have been returned. 
I tested /players/playerID endpoint with test_get_player() and 
test_get_player_that_does_not_exist()

5) ## Dockerize Your Application: 

I wrote a Dockerfile to package my application into a Docker image

FROM python

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "./services/players.py"] 

STOPSIGNAL SIGINT



6) ## Test Endpoints
To test endpoint after completing the previous steps, I followed these instructions:

a.	Build the Docker Image: First, i built the Docker image using the Dockerfile I created by navigating to the directory containing my Dockerfile and ran the following command:

docker build -t player-microservice . 

b.	Run the Docker Container: Once the image is built, I then run a Docker container based on that image using the following command: 

docker run -p 5000:5000 --name services player-microservice    --- initial command to run docker and create container/image

c.	Access the Endpoints: With the Docker container running, I  accessed my REST endpoints by opening a web browser and Postman to send HTTP requests to endpoints. 

•	To retrieve all players: http://localhost:5000/players

•	To retrieve a single player by ID: http://localhost:5000/players/playerID, where playerID is the ID of the player you want to retrieve.

d.	Test Endpoints:I verified that my endpoints are functioning correctly by checking the responses. I used Postman to send GET requests to my endpoints and examined the returned JSON data.
   
