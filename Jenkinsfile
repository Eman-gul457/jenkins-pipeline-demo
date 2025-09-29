pipeline {
  agent any

  environment {
    IMAGE = 'jenkins-flask-app'
    CONTAINER = 'jenkins-flask-app-container'
    ARCHIVE = '/var/lib/jenkins/project.tar.gz'
  }

  stages {
    stage('Prepare Workspace') {
      steps {
        script {
          echo "Using archive from: ${ARCHIVE}"
          sh "cp ${ARCHIVE} ./project.tar.gz"
          sh "tar -xvzf project.tar.gz"
          sh "ls -la"
        }
      }
    }

    stage('Build Docker image') {
      steps {
        sh "docker build -t ${IMAGE} ."
      }
    }

    stage('Run container') {
      steps {
        sh "docker rm -f ${CONTAINER} || true"
        sh "docker run -d -p 5000:5000 --name ${CONTAINER} ${IMAGE}"
      }
    }

    stage('Smoke test') {
      steps {
        sh "sleep 3"
        sh "curl -s -f http://localhost:5000 || (echo 'App did not respond' && false)"
      }
    }
  }

  post {
    success {
      echo "✅ SUCCESS — App running at http://localhost:5000"
    }
    failure {
      echo "❌ FAILED — Check logs"
    }
  }
}
