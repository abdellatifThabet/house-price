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
                //sh 'fuser -n tcp -k 5000 | true'
                sh'docker kill $(docker ps -q) | true'
                echo 'connecting to the docker hub'
                sh 'docker login -u "abdou2020" -p "abdou54460380"'
                echo 'Build the docker image'
                //sh 'docker build -t abdou2020/houce-price-app .'
                echo 'push to my docker hub'
                //sh 'docker push abdou2020/houce-price-app'
                echo 'running container on localhost for testing'
                sh 'docker run -d -p 5000:5000 abdou2020/houce-price-app'
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
            echo 'if test passes we will run the docker container on our vp server'  
        }
        success {
            echo 'deploying our app on the vps'
            echo 'connecting to the vps ...'
            //sh 'sshpass -p "7Yd4Ya9pyNdf" ssh -o StrictHostKeyChecking=no ubuntu@51.254.126.68'
            sh 'scp remote-cmds.sh ubuntu@51.254.126.68:/home/ubuntu/'
            echo "pulling the image and running the container "
            sh 'ssh ubuntu@51.254.126.68 "sh remote-cmds.sh"'

        }
        failure {
            echo 'the app failed in the test stage'
        }


    }
}
