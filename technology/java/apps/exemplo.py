from datetime import time

import docker
import logger
from docker.errors import BuildError


def build(secrets, to_path, app_name_git, branch_tag):
    tag_name = app_name_git + ":" + branch_tag
    client = docker.from_env()
    try:
        print("Building Image...")
        i, log = client.images.build(path=to_path,
                                     dockerfile="Dockerfile",
                                     tag=tag_name,
                                     nocache=True,
                                     rm=True,
                                     forcerm=True,
                                     pull=True)
        for line in log:
            print(line)
        print('Done')
        re_deploy = redeployment(secrets, tag_name, app_name_git)
        if re_deploy is None:
            deployment(secrets, tag_name, app_name_git)
    except BuildError as e:
        print("Hey something went wrong with image build!")
        for line in e.build_log:
            if 'stream' in line:
                logger.error(line['stream'].strip())
        raise


def redeployment(secrets, tag_name, app_name_git):
    client = docker.from_env()
    try:
        for container_check in client.containers.list(all=True, filters={"name": app_name_git}):
            if container_check:
                container_delete = client.api.remove_container(container=container_check.name, force=True)
                print('Container Removed')
                print('Deploying Container...')
                container = client.containers.run(image=tag_name,
                                                  detach=True,
                                                  ports={'8080/tcp': 8085},
                                                  name=app_name_git,
                                                  environment=secrets)
                process = container.logs(stream=True, follow=False)

                for line in process:
                    print(line)
                return container.id
    except BuildError as e:
        print(e)
        raise Exception(e)


def deployment(secrets, tag_name, app_name_git):
    client = docker.from_env()
    print('Deploying Container...')
    try:
        container = client.containers.run(image=tag_name,
                                          detach=True,
                                          ports={'8080/tcp': 8085},
                                          name=app_name_git,
                                          environment=secrets)
        process = container.logs(stream=True, follow=False)
        print('Container Deployed..')
        for line in process:
            print(line)
    except BuildError as e:
        print(e)
        raise Exception(e)
