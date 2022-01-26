pipeline {
    agent any
    parameters{
        booleanParam(name:'validTest', defaultValue : true,description : '')
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

            steps {
                echo 'kill on port 5000 before running the container'
                sh 'kill -9 $(lsof -t -i:5000) || true'
                echo 'Build the docker image'
                sh 'docker build -t houce-price-app .'
                echo 'running the container'
                sh 'docker run -d -p 5000:5000 houce-price-app'
                
            }
        }
          
         
        stage('Test') {


            steps {
                echo 'gui testing using selenium webdriver'
                sh 'sh auto-test.sh'       
                sh 'if [ $? -eq 0 ]; then echo test succeded; else test failed ;fi'        
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
