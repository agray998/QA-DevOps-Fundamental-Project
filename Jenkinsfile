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
                sh "/bin/bash -c 'docker rmi \$(docker images -q)'"
                sh "docker-compose build --parallel"
                sh "docker login -u ${DOCKER_CREDS_USR} -p ${DOCKER_CREDS_PSW}"
                sh "docker-compose push"
            }
        }
        stage('deploy stack') {
            steps {
                sh "echo '    driver: overlay' >> docker-compose.yaml"
                sh "scp ./docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml"
                sh "scp ./nginx.conf jenkins@swarm-manager:/home/jenkins/nginx.conf"
                sh "ssh jenkins@swarm-manager < deploy.sh"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "flask-app/htmlcov/*"
        }
    }
}