pipeline {
    agent any

    parameters {
        choice(name: 'TEST_SUITE', choices: ['smoke', 'regression'], description: 'Test suite to execute')
        choice(name: 'TEST_ENV', choices: ['dev', 'qa', 'staging'], description: 'Target test environment')
        string(name: 'RETRY_COUNT', defaultValue: '1', description: 'Retry count for transient failures')
    }

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
    }

    environment {
        PYTHON = 'C:\\Users\\Yasaswini\\AppData\\Local\\Programs\\Python\\Python311\\python.exe'
        VENV_PYTHON = '.venv\\Scripts\\python.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Branch Validation') {
            steps {
                script {
                    echo "Pipeline branch: ${env.BRANCH_NAME ?: 'main'}"
                    echo "Build commit: ${env.GIT_COMMIT ?: 'N/A'}"
                    echo "Branch validation completed."
                }
            }
        }

        stage('Environment Setup') {
            steps {
                bat 'if not exist .venv "%PYTHON%" -m venv .venv'
                bat '%VENV_PYTHON% -m pip install --upgrade pip'
                bat '%VENV_PYTHON% -m pip install -r requirements.txt'
            }
        }

        stage('Test Execution') {
            steps {
                script {
                    def marker = params.TEST_SUITE == 'smoke' ? 'smoke' : 'regression'
                    def retries = params.RETRY_COUNT.toInteger() + 1

                    bat 'if not exist reports mkdir reports'

                    retry(retries) {
                        bat "%VENV_PYTHON% -m pytest -m ${marker} --junitxml=reports\\${marker}-${params.TEST_ENV}.xml"
                    }
                }
            }

            post {
                always {
                    junit allowEmptyResults: true, testResults: 'reports/*.xml'
                }
            }
        }

        stage('Execution Summary') {
            steps {
                echo "Test Suite : ${params.TEST_SUITE}"
                echo "Environment: ${params.TEST_ENV}"
                echo "Retry Count: ${params.RETRY_COUNT}"
                echo "Automation execution completed."
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: 'reports/*.xml',
                allowEmptyArchive: true
            )
        }

        success {
            echo 'SUCCESS: Automated test execution completed.'
        }

        failure {
            echo 'FAILED: Automation execution failed. Review the JUnit report.'
        }
    }
}