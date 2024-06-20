pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/nikodemplocki/lab12zad1.git'
            }
        }

        stage('Test') {
            steps {
                script {
                    // Utwórz wirtualne środowisko Pythona
                    sh 'python3 -m venv myenv'

                    // Aktywuj wirtualne środowisko i zainstaluj zależności
                    sh 'source myenv/bin/activate && pip install -r requirements.txt'

                    // Uruchom testy jednostkowe
                    sh 'source myenv/bin/activate && python3 -m unittest test_calculator.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment completed successfully'
                // Dodatkowe kroki wdrażania, jeśli są potrzebne
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
