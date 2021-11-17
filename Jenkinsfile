@Library('pipelinex@development') _
import com.iguazio.pipelinex.DockerRepo

workDir = '/home/jenkins'
podLabel = 'mlrun-ltm'
//def ltm_mlrun_output = ''

properties_args = [
    parameters([
        string(defaultValue: 'Hedi Ingber', description: 'user name', name: 'user_name', trim: true),
    ]),
]

podTemplate(
    label: podLabel,
    containers: [
        containerTemplate(name: 'base-build', image: 'iguazioci/alpine-base-build:ae7e534841e68675d15f4bd98f07197aed5591af', workingDir: workDir, ttyEnabled: true, command: 'cat'),
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

                    stage("build  pipeline for ${params.user_name}") {
                        println("Test LTM pipeline")
                        println(common.shellc("USER_NAME=${params.user_name}; ltm_mlrun_command.bsh $USER_NAME"))
                    }

               }
            }
        }
    }
}
