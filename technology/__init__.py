from technology.java import JavaDeploy


class DeployApps:

    @staticmethod
    def deploy_apps(technology, apps, env, vault_envs, to_path, branch_tag):
        match technology:
            case java:
                deploy_java = JavaDeploy()
                return deploy_java.deploy_java_app(apps, env, vault_envs, to_path, branch_tag)
