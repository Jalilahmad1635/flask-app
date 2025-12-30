pipeline {
    agent any

    environment {
        APP_DIR  = "flask"
        VENV_DIR = "venv"
        PYTHON   = "C:\\msys64\\ucrt64\\bin\\python.exe"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning GitHub repository"
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir("${APP_DIR}") {
                    bat """
                        "%PYTHON%" -m venv ..\\%VENV_DIR%
                        ..\\%VENV_DIR%\\bin\\python -m pip install Flask pytest
                    """
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                dir("${APP_DIR}") {
                    bat """
                        ..\\%VENV_DIR%\\bin\\pytest
                    """
                }
            }
        }

        stage('Build Application') {
            steps {
                echo "Building Flask application"
                dir("${APP_DIR}") {
                    bat """
                        ..\\%VENV_DIR%\\bin\\python -m py_compile app.py
                    """
                }
            }
        }

        stage('Deploy Application') {
            steps {
                echo "Deploying application to production environment"
                echo "Application deployed successfully"
            }
        }
    }
}
