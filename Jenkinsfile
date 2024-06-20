pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }

    post {
        always {
            junit '**/test-*.xml'
            archiveArtifacts artifacts: '**/test-*.xml', allowEmptyArchive: true
        }
    }
}
