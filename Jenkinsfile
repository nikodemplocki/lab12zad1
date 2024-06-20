pipeline {
    agent any

    triggers {
        scm '* * * * *'  // Trigger pipeline on every commit
    }

    stages {
        stage('Test') {
            steps {
                script {
                    sh 'python3 -m unittest test_calculator.py'  // Run unit tests
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
        always {
            // Clean up or additional steps to run after pipeline completes
        }

        success {
            echo 'Pipeline succeeded!'
        }

        failure {
            echo 'Pipeline failed :('
        }
    }
}
