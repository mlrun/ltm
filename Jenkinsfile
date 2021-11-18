@Library('pipelinex@development') _
import com.iguazio.pipelinex.DockerRepo

workDir = '/home/jenkins'
podLabel = 'mlrun-ltm'

properties([
    parameters([
        string(defaultValue: 'Hedi Ingber', description: 'user input', name: 'user_input'),
    ])
])

podTemplate(
    label: podLabel,
    containers: [
        containerTemplate(name: 'base-build', image: 'busybox', workingDir: workDir, ttyEnabled: true, command: 'cat'),
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
                        println("Test LTM pipeline for ${env.user_input}")
                        script {
                                  sh('echo ${env.user_input}')
                               }
                    }

               }
            }
        }
    }
}
