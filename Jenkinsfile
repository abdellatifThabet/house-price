pipeline {
  agent any
  stages {
    stage('Building image') {
      steps{
             echo 'starting the build'
             sh 'docker build -t home-pricing-app .'
             sh 'docker run -d -port 5000:5000 home-pricing-app'
      }
    }


