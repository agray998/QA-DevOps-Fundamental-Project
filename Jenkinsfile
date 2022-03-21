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
        stage('build and push') {
            environment {
                DOCKER_CREDS = credentials('docker-creds')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u ${DOCKER_CREDS_USR} -p ${DOCKER_CREDS_PSW}"
                sh "docker-compose push"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "flask-app/htmlcov/*"
        }
    }
}