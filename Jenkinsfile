@Library('eliox-jenkins-shared-library@develop') _

pipeline {
  agent any

  parameters {
    booleanParam(name: 'DEPLOY', defaultValue: true, description: 'Ejecutar deploy')
    string(name: 'DEPLOY_IMAGE_TAG', defaultValue: 'latest', description: 'Tag de imagen Docker')
    choice(name: 'ENV', choices: ['dev', 'staging', 'prod'], description: 'Environment lógico')
    string(name: 'KUBECONFIG_CREDENTIALS_ID', defaultValue: 'kubeconfig-bootstrap-kind', description: 'Jenkins Secret file ID')
  }

  stages {
    stage('Run shared library') {
      steps {
        script {
          enterprisePipeline([
            appName: 'mc-user-fastapi',
            deploy: params.DEPLOY,
            environment: params.ENV,
            agentLabel: 'built-in',

            kubeconfigCredentialsId: params.KUBECONFIG_CREDENTIALS_ID,
            deployRepoUrl: 'https://github.com/elioxrome/eliox-platform-config',
            deployRepoBranch: 'main',
            helmChartPath: "charts/mc-user-fastapi",
            deployNamespace: 'apps',
            kindClusterName: 'local-cluster',
            deployImageTag: params.DEPLOY_IMAGE_TAG
          ])
        }
      }
    }
  }
}
