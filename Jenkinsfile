pipeline {
    agent any
    parameters{
        booleanParam(name:'executeTest', defaultValue : true,description : '')
    }
    environment {
        NEW_VERSION = "1.0"
    }
    stages {
        stage('git cloning') {
            steps {
                echo 'git cloning stage'
                git 'https://github.com/abdellatifThabet/house-price'
            }            
        }
        stage('Build') {
            when{
                expression{
                    params.executeTest && env.BRANCH_NAME == 'master'
                }
            }
            steps {
                echo 'Build the docker image'
                sh 'docker build -t houce-price-app .'
                echo 'running the container'
                sh 'docker run -d -p 5000:5000 houce-price-app'
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deployment stage does not exist for ow'
            }            
        }
    }
    post{
        always {
            echo 'this will always be run'  
        }
        success {
            echo 'this will be run only if the build succeeded'
        }
        failure {
            echo 'this will be run in case of failure'
        }


    }
}
