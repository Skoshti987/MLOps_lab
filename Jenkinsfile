
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
                echo 'Code retrieved from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v -s'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat '.venv\\Scripts\\python.exe monitoring.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'evidently_report.html', allowEmptyArchive: true
        }
    }
}
