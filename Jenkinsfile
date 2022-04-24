pipeline {
    agent any
    stages {
    stage('Deploy') {
      options {
        timeout(time: 200, unit: 'SECONDS') 
      }
      steps {
         script {
          mail body: "<br>Jenkins Job Name: ${env.JOB_NAME}<br> Git Repo name: ${REPO_NAME} <br> Mail id: ${MAIL_ID} <br> User name: ${env.NAME} <br> Please check and approve/reject the request? <br> Approval URL: ${env.BUILD_URL}console",charset: 'UTF-8', mimeType: 'text/html', subject: "Github Repo Creation Approval Request", to: "subham.devops@gmail.com,subham.rhce@gmail.com";
          def USER_INPUT = input(message: 'Please Review This Request?',
            parameters: [[$class: 'ChoiceParameterDefinition',choices: ['Yes','No'].join('\n'),name: 'CHOICE',description: 'Please select "Yes" to Approve and "No" to Decline']])
            echo "The answer is: ${USER_INPUT}"
            if( "${USER_INPUT}" == "Yes"){
               echo "Git repo $REPO_NAME is being created with mail ID $MAIL_ID"
            } else {
               echo "Here am running as No"
            }
        }
      }
      }
    }
    }
