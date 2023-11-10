from constants import environment
from deployment import structures
from technology import DeployApps
from git import Repo


class GenericDeployment:
    @staticmethod
    def check_language(technology=environment.DEFAULT_TECHNOLOGY):
        if technology is None:
            raise ImportError("Export Environment Variable DEFAULT_TECHNOLOGY in Pipe")
        else:
            print("Default Language form pipe is " + technology)
        return technology

    @staticmethod
    def check_env(env=environment.ENVIRONMENT):
        if env is None:
            raise ImportError("Export Environment Variable ENVIRONMENT in Pipe")
        else:
            print("Deploy environment is " + env)
        return env

    @staticmethod
    def check_app(app=environment.APP, app_git=environment.APP_NAME_GIT):
        if app is None:
            raise ImportError("Export Environment Variable APP_NAME in Pipe")
        else:
            print("Deployment Application is " + app)

        if app_git is None:
            raise ImportError("Export Environment Variable APP_NAME_GIT in Pipe")
        else:
            print("Name of git repository is " + app_git)
        return app, app_git

    @staticmethod
    def check_branch_tag(repo=environment.BRANCH_TAG):
        if repo is None:
            raise ImportError("Export Environment Variable BRANCH_TAG in Pipe")
        else:
            print("Branch or Tag is " + repo)
        return repo

    @staticmethod
    def prepare_env():
        return structures.prepare_folders()

    @staticmethod
    def git_clone():
        Generic = GenericDeployment()
        to_path = Generic.prepare_env()
        branch = Generic.check_branch_tag()
        app_name_git = Generic.check_app()
        repo_url = "https://github.com/" + environment.GIT_PROJECT + "/" + app_name_git[1] + ".git"
        Repo.clone_from(repo_url, to_path, branch=branch, depth=1)
        print("Clone Repository Success in " + to_path)

    @staticmethod
    def vault_env(vault_url=environment.VAULT_URL, role_id=environment.VAULT_ROLE_ID,
                  secret_id=environment.VAULT_SECRET_ID):

        print("Vault Endpoint is " + vault_url)

        if role_id is None:
            raise ImportError("Export Environment Variable VAULT_ROLE_ID in Pipe")
        else:
            print("Vault Role is " + role_id)

        if secret_id is None:
            raise ImportError("Export Environment Variable VAULT_SECRET_ID in Pipe")
        else:
            print("Vault Secret ok ")
        return vault_url, role_id, secret_id

    @staticmethod
    def deploy_app():
        Generic = GenericDeployment()
        tec = Generic.check_language()
        new_app = Generic.check_app()
        env = Generic.check_env()
        vault_envs = Generic.vault_env()
        deploy = DeployApps()
        to_path = environment.DEFAULT_WORKSPACE + environment.APP + "/current"
        branch_tag = Generic.check_branch_tag()
        return deploy.deploy_apps(tec, new_app, env, vault_envs, to_path, branch_tag)

    @staticmethod
    def pipe():
        Generic = GenericDeployment()
        return (
            Generic.check_language(),
            Generic.check_env(),
            Generic.check_app(),
            Generic.prepare_env(),
            Generic.git_clone(),
            Generic.deploy_app()
        )


deployment = GenericDeployment()
deployment.pipe()
