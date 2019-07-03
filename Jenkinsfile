def FAILED_STAGE = null

pipeline{
    agent {
        label 'testci'
    }
    environment {
        GITLAB_COMMON_CREDS = credentials('0f283a85-77da-4bb5-9d53-1d50e1e16608')
    }
    stages{
        stage('checkout code'){
            steps{
                script {FAILED_STAGE = env.STAGE_NAME}
                git branch: 'test', credentialsId: '7a995ee0-a7bf-406d-8373-c17778085066', url: 'https://github.com/joystitch/Python.git'
            }

        }
    }

    post{
        failure{
            echo "failed! please check the test result!"
        }
        success{
            echo "success!"
        }
    }
}

