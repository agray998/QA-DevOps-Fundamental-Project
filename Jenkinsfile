pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh "rm flask-app/application/tests/test_int*"
                sh "bash flask-app/test_basic.sh"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "htmlcov/*"
        }
    }
}