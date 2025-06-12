pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_NAME = 'nivemuthu09/fraud-detector-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_HUB_CREDENTIALS}") {
                        def app = docker.build("nivemuthu09/fraud-detector-app:latest", ".")
                        app.push()
                    }
                }
            }
        }

        stage('Deploy via Helm') {
            steps {
                sh '''
                helm upgrade --install my-fraud-detector ./helm-chart \
                  --set image.repository=nivemuthu09/fraud-detector-app \
                  --set image.tag=latest
                '''
            }
        }
    }
}

