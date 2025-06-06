pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_NAME = 'nivemuthu09/fraud-detector-app'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/nivemukr09/fraud-detector-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest ./app'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }
    }
}

