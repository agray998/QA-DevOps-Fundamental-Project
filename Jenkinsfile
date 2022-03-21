pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh "bash test_basic.sh"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "htmlcov/*"
        }
    }
}