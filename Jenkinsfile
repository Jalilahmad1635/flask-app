pipeline {
    agent any

    environment {
        APP_DIR  = "flask"
        VENV_DIR = "venv"
    }

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir("${APP_DIR}") {
                    bat """
                        py -m venv ..\\%VENV_DIR%
                        ..\\%VENV_DIR%\\Scripts\\pip install --upgrade pip
                        ..\\%VENV_DIR%\\Scripts\\pip install -r requirements.txt
                        ..\\%VENV_DIR%\\Scripts\\pip install pytest
                    """
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                dir("${APP_DIR}") {
                    bat """
                        ..\\%VENV_DIR%\\Scripts\\pytest
                    """
                }
            }
        }

        stage('Build Application') {
            steps {
                dir("${APP_DIR}") {
                    bat """
                        ..\\%VENV_DIR%\\Scripts\\python -m py_compile app.py
                    """
                }
            }
        }

        stage('Deploy Application') {
            steps {
                dir("${APP_DIR}") {
                    bat """
                        echo Deploying Flask Application
                        ..\\%VENV_DIR%\\Scripts\\python app.py
                    """
                }
            }
        }
    }
}
