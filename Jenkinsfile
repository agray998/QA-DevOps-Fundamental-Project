pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                dir('flask-app') {
                    sh "rm application/tests/test_int*"
                    sh "bash test_basic.sh"
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "${WORKSPACE}/htmlcov/*"
        }
    }
}