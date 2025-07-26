pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/hardik0501/FeedbackCiCD.git'
            }
        }

        stage('Stop Existing Container (Port 5000)') {
            steps {
                bat '''
                docker ps -q --filter "publish=5000" | for /F %%i in ('more') do docker stop %%i || exit 0
                docker ps -a -q --filter "publish=5000" | for /F %%i in ('more') do docker rm %%i || exit 0
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t feedback-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name feedback-container feedback-app'
            }
        }
    }
}
