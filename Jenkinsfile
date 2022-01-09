pipeline {
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/abdellatifThabet/house-price.git'                              
      }
    }
    stage('Building image') {
      steps{
             sh 'docker build -t home-pricing-app .'
             sh 'docker run -d -port 5000:5000 home-pricing-app'
      }
    }


