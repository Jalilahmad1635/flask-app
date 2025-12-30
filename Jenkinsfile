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
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir("${APP_DIR}") {
                    bat """
                        "%PYTHON%" -m venv ..\\%VENV_DIR%
                        ..\\%VENV_DIR%\\bin\\pip install --upgrade pip
                        ..\\%VENV_DIR%\\bin\\pip install -r requirements.txt
                        ..\\%VENV_DIR%\\bin\\pip install pytest
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
                dir("${APP_DIR}") {
                    bat """
                        ..\\%VENV_DIR%\\bin\\python -m py_compile app.py
                    """
                }
            }
        }

        stage('Deploy Application') {
            steps {
                dir("${APP_DIR}") {
                    bat """
                        echo Deploying Flask Application
                        ..\\%VENV_DIR%\\bin\\python app.py
                    """
                }
            }
        }
    }
}
