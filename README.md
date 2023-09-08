# Reflex Portfolio

## Description
This is a portfolio that I created to showcase my work. It is a single page application that shows my projects, contact information, and a little bit about me. My CV is also available for download. The application is built using only Reflex with Python. The application is deployed using Docker and Docker Compose.

## Installation
To install the necessary dependencies, run the following command:
```
pip install reflex
```

## Usage
To use this application, run the following command:
```
reflex init
reflex run
```

## Deployment
To dockerize this application, the Dockerfile is used:
```
docker build -t my_portfolio .
```

And then the docker-compose.yml file is used to deploy the application:
```
docker-compose up -d
```



