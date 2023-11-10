import importlib
from technology.java.apps import exemplo
from vault import vault


class JavaDeploy:

    @staticmethod
    def deploy_java_app(apps, env, vault_envs, to_path, branch_tag):
        try:
            new_deploy = JavaDeploy()
            check_secrets = new_deploy.get_secrets(apps[0], env, vault_envs)
            new_module = importlib.import_module(f"technology.java.apps.{apps[0]}")
            new_module.build(check_secrets, to_path, apps[1], branch_tag)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_secrets(apps, env, vault_envs):
        url = vault_envs[0]
        role_id = vault_envs[1]
        secret_id = vault_envs[2]
        new_vault = vault.VaultManager(url, role_id, secret_id)
        new_vault.authenticate()
        secrets = new_vault.read_secret(env, apps)
        return secrets
