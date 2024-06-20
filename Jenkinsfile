pipeline {
    agent any

    triggers {
        cron('* * * * *')  // Trigger pipeline on every minute
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository before running any other steps
                git 'https://github.com/nikodemplocki/lab12zad1.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    // Install dependencies if needed
                    sh 'pip install -r requirements.txt'

                    // Run unit tests
                    sh 'python3 -m unittest test_calculator.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Additional deployment steps can go here if needed
                    echo 'Deployment completed successfully'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }

        failure {
            echo 'Pipeline failed :('
        }
    }
}
