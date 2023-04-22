# IDS721 Final Project

## Introduction
This is the final project for the course IDS721, it is an image recognition web application built using Flask, Python, and TensorFlow. Users can upload an image, and the application will return the original image along with labels describing the content of the image. I used the Docker image to deploy this application and created a repository in DockerHub so that everyone could run it easily without cloning the whole project. Also, I depolyed this app on the AWS App Runner.

## Features

* Simple and clean user interface
* Upload images in various formats (jpg, jpeg, png, gif)
* Utilizes MobileNetV2 model for image recognition
* Displays top 5 predicted labels with probabilities

## Function Display
___Home Page:___   

<img src="https://github.com/Gary-Zhigang/IDS721-Final_Project/blob/main/images/p1.png" alt="Your image description" width="600" height="400">

___Result Page:___  

<img src="https://github.com/Gary-Zhigang/IDS721-Final_Project/blob/main/images/p2.png" alt="Your image description" width="600" height="600"> 

## Docker 
___Local:___   

After you clone this project, to build the Docker in local, you could type ``docker build -t image-recognition``, and then type ``docker image ls`` to verify the images you get, finally, typing ``docker run -p 8080:8080 image-recognition`` to run the application.

___DockerHub:___  

You could also run the Docker without cloning this project, you could pull the image from the **DockerHub** by typing ``docker pull zhiw803/image-recognition:latest``, and then typing ``docker run -p 8080:8080 zhiw803/image-recognition:latest`` to run the application.

## AWS App Runner

You could click [this link](https://sy2ueazacf.us-east-1.awsapprunner.com) to explore the image recognition website, which is deployed on the AWS App Runner.

<img src="https://github.com/Gary-Zhigang/IDS721-Final_Project/blob/main/images/p3.png" alt="Your image description" width="750" height="350"> 
