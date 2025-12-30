pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
        APP_DIR  = "flask"
    }

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python + Install Dependencies') {
            steps {
                dir("${APP_DIR}") {
                    sh '''
                        python3 -m venv ../${VENV_DIR}
                        ../${VENV_DIR}/bin/pip install --upgrade pip
                        ../${VENV_DIR}/bin/pip install -r requirements.txt
                        ../${VENV_DIR}/bin/pip install pytest
                    '''
                }
            }
        }

        stage('Unit Tests (pytest)') {
            steps {
                dir("${APP_DIR}") {
                    sh '''
                        ../${VENV_DIR}/bin/pytest -q || exit 1
                    '''
                }
            }
        }

        stage('Build Application') {
            steps {
                dir("${APP_DIR}") {
                    sh '''
                        echo "Build step: packaging / sanity check"
                        ../${VENV_DIR}/bin/python -m py_compile app.py
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                dir("${APP_DIR}") {
                    sh '''
                        echo "Deploy step (demo): starting Flask app"
                        echo "In real deploy you would systemctl restart / docker build+run / kubectl apply"
                        nohup ../${VENV_DIR}/bin/python app.py > ../app.log 2>&1 &
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'app.log', allowEmptyArchive: true
        }
    }
}
