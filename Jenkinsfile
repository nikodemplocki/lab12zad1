pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install unittest-xml-reporting
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                python -m xmlrunner discover -o test-reports
                '''
            }
        }
    }

    post {
        always {
            junit 'test-reports/*.xml'
            archiveArtifacts artifacts: 'test-reports/*.xml', allowEmptyArchive: true
        }
    }
}
