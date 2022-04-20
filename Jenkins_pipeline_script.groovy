pipeline {
    agent any
    environment {
        dockerImage =''
        registry = "janeethreddy/task1"
        registryCredential = 'dockerhub'
    }
    
    stages {
        stage('Checkout'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/JaneethReddy/Viridios-Task1.git']]])
            }
        }
        
       stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
  }
}