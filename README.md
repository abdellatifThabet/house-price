# housePricesDemo
CICD pipeline for houce price flask web app to predict the price of a houce using jenkins.
## The pipeline is composed of three main stages:
### build stage: building a docker image for the app and run the container on localhost for testing 
### test stage: test the app using selenium python library
### deployment stage : which will only be run if the test stage succeeded and in this stage i have deployed the app on my vps server
