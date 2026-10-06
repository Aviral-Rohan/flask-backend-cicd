// CI/CD pipeline for the Flask backend
pipeline {
    agent any

    // Runs automatically when GitHub sends a push webhook
    triggers {
        githubPush()
    }

    // Settings used by the stages below (no secrets are stored in this file)
    environment {
        APP_DIR    = '/opt/apps/flask-backend'
        SERVICE    = 'flask-backend'
        HEALTH_URL = 'http://localhost:5000/health'
    }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull the latest code from the Git repository into the Jenkins workspace
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Deploy') {
            steps {
                // Update the live copy of the app, install its dependencies, restart the service
                sh '''
                    sudo -u ubuntu git -C "$APP_DIR" pull --ff-only
                    sudo -u ubuntu "$APP_DIR/venv/bin/pip" install -r "$APP_DIR/requirements.txt"
                    sudo systemctl restart "$SERVICE"
                '''
            }
        }

        stage('Health check') {
            steps {
                sh '''
                    sleep 5
                    curl --fail --silent --show-error "$HEALTH_URL"
                '''
            }
        }
    }

    post {
        success { echo 'Flask backend deployed successfully.' }
        failure { echo 'Pipeline failed. The running application was not changed by a failed test.' }
    }
}
