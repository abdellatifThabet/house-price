pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build the docker image'
                sh 'docker build -t houce-price-app .'
                echo "running the container"
                sh 'docker run -d -p 5000:5000 houce-price-app'
                
            }
        stage('Deploy') {
            steps {
                echo 'Deployment stage does not exist for ow'
            }            
        }
    }
}
