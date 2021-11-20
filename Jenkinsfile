@Library('pipelinex@development') _
import com.iguazio.pipelinex.DockerRepo

workDir = '/home/jenkins'
podLabel = 'mlrun-ltm'

properties([
    parameters([
        string(defaultValue: 'mustprovide', description: 'MLRun API URL', name: 'MLRUN_DBPATH'),
        string(defaultValue: 'mustprovide', description: 'V3IO API URL', name: 'V3IO_API'),
        string(defaultValue: 'mustprovide', description: 'V3IO username', name: 'V3IO_USERNAME'),
        string(defaultValue: 'mustprovide', description: 'V3IO access key', name: 'V3IO_ACCESS_KEY'),
        string(defaultValue: 'mustprovide', description: 'MLRun project name', name: 'PROJECT_NAME'),
    ])
])

podTemplate(
    label: podLabel,
    containers: [
        containerTemplate(name: 'base-build', image: 'mlrun/mlrun:0.9.0-rc2' , ttyEnabled: true, command: 'cat'),
    ],
    volumes: [
        hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'),
    ],
) {
    node(podLabel) {
        common.notify_slack {
            withCredentials([
                string(credentialsId: 'iguazio-prod-git-user-token', variable: 'GIT_TOKEN')
            ]) {

                container('base-build') {
                    stage("git clone") {
                        checkout scm
                        }

                    stage("build  pipeline for ${env.user_input}") {
                        sh """ MLRUN_DBPATH=${env.MLRUN_DBPATH} V3IO_API=${env.V3IO_API} V3IO_USERNAME=${env.V3IO_USERNAME} V3IO_ACCESS_KEY=${env.V3IO_ACCESS_KEY} mlrun project -r main -n ${env.PROJECT_NAME} -w ./ """

                    }

               }
            }
        }
    }
}
