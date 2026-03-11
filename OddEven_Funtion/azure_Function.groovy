pipeline {
    agent any
    environment {
        // Update these with your specific Azure details
        AZURE_TENANT_ID = 'c86fb52a-d57e-4969-9927-e0076d423274'
        AZ_SUBSCRIPTION = 'c06686e2-d368-48c1-936d-cf7a2f342148'
        RES_GROUP       = 'myFunctionGroup' 
        FUNC_APP_NAME   = 'odd-even-api-test'
        git_Url="https://github.com/SudhirDevange/Python.git"
    }
    stages {
        stage('Checkout') {
            steps {
                deleteDir()
                echo "Git checkout, ${git_Url}"
                checkout scmGit(branches: [[name: '*/main']],
                extensions: [sparseCheckout([[path: 'OddEven_Funtion/*']])], 
                userRemoteConfigs: [[url: "${git_Url}"]])
            }
        }
        stage('Deploy to Azure') {
            steps {
                // This block securely injects your AppId and Secret
                withCredentials([usernamePassword(credentialsId: 'azure_functions_sp', passwordVariable: 'SP_PASS', usernameVariable: 'SP_ID')]) {
                    powershell """
                        # Login to Azure
                        az login --service-principal -u "${SP_ID}" -p "${SP_PASS}" -t "${AZURE_TENANT_ID}"
                        az account set -s "${AZ_SUBSCRIPTION}"

                        # Create Zip using PowerShell (Excluding venv and .git)
                        # We filter files first, then pipe to Compress-Archive
                        Get-ChildItem -Path OddEven_Funtion -Exclude "venv", ".git", "deploy.zip" | Compress-Archive -DestinationPath deploy.zip -Force

                        # Deploy to Azure
                        #az functionapp deployment source config-zip -g "${RES_GROUP}" -n "${FUNC_APP_NAME}" --src deploy.zip
                        az functionapp deployment source config-zip -g "${RES_GROUP}" -n "${FUNC_APP_NAME}" --src deploy.zip --build-remote true

                        # Logout
                        az logout
                    """
                }
            }
        }
    }
}
