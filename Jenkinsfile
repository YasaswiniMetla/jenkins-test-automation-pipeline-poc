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

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Branch Validation') {
            steps {
                script {
                    def allowed = ['main', 'develop']
                    def branch = env.BRANCH_NAME ?: sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()

                    echo "Executing branch: ${branch}"

                    if (!allowed.contains(branch)) {
                        echo "Warning: ${branch} is not a protected release branch."
                    }
                }
            }
        }

        stage('Environment Setup') {
            steps {
                sh 'python3 -m venv .venv || true'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test Execution') {
            steps {
                script {
                    def marker = params.TEST_SUITE == 'smoke' ? 'smoke' : 'regression'

                    retry(params.RETRY_COUNT.toInteger() + 1) {
                        sh ".venv/bin/pytest -m ${marker} --junitxml=reports/${marker}-${params.TEST_ENV}.xml"
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
                echo "Suite      : ${params.TEST_SUITE}"
                echo "Environment: ${params.TEST_ENV}"
                echo "Status     : ${currentBuild.currentResult}"
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.xml', allowEmptyArchive: true
        }
        success {
            echo 'Automation execution completed successfully.'
        }
        failure {
            echo 'Automation execution failed. Review the published JUnit report.'
        }
    }
}
