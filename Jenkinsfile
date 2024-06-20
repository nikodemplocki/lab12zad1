pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Setup') {
            steps {
                sh 'pip3 install unittest-xml-reporting'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m xmlrunner discover -o test-reports'
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
