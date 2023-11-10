import hvac


class VaultManager:

    def __init__(self, url, role_id, secret_id):
        self.url = url
        self.role_id = role_id
        self.secret_id = secret_id
        self.client = hvac.Client(url, verify=False)
        self.client.auth.approle.login(role_id, secret_id)

    def authenticate(self):
        if not self.client.is_authenticated():
            raise ValueError("Vault failed authentication.")
        # new_token = self.client.auth
        # print(new_token)
        print("Vault authenticated success!")
        return self.client

    def read_secret(self, env, apps):
        response = self.client.secrets.kv.v2.read_secret_version(path=env, mount_point=apps)
        try:
            return response['data']['data']
        except Exception as e:
            print(e)
