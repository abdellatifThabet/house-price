pipeline {
   agent any
   parameters{
      booleanParam(name:'executeTest', defaultValue : true,description : '')
   }
   environment {
   NEW_VERSION = "1.0"
      }
   stages{
      stage("build"){
        steps{
           when{
              expression{
                 params.executeTest
              }
           }
           echo "building the app"
           echo "building the version ${NEW_VERSION}"
        
        }
     }
      stage("test"){
        steps{
           echo "testing the app"  
        
        }
     }
  
   }

}
