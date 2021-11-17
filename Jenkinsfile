@Library('pipelinex@development') _
import com.iguazio.pipelinex.DockerRepo

workDir = '/home/jenkins'
podLabel = 'mlrun-ltm'
//def ltm_mlrun_output = ''

properties_args = [
    parameters([
        string(defaultValue: 'Hedi Ingber', description: 'user name', name: 'user_name', trim: true)
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
                        println("Test LTM pipeline")
                        //ltm_mlrun_output =
                        //sh(script: "./ltm_mlrun_command.bsh ${params.user_name}", returnStdout: true)
                        sh('ltm_mlrun_command.bsh ${params.user_name}')
                        //writeFile(file: "ltm_mlrun_output.txt", text: ltm_mlrun_output)
                    }
               }
            }
        }
    }
}
