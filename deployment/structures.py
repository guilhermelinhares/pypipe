import os
import shutil
from constants import environment


def prepare_folders(workspace=environment.DEFAULT_WORKSPACE, app=environment.APP):
    """
        @param workspace: Where's deployment app
        @param app: Application Name
    """
    path = workspace + app
    path_current = path + "/current"
    path_shared = path + "/shared"
    path_public = path_shared + "/public"
    path_log = path_shared + "/log"
    path_certs = path_shared + "/certs"

    if not os.path.exists(path):
        os.mkdir(path)
        print("Folder %s created!" % path)
    else:
        print("Folder %s already exists" % path)

    if not os.path.exists(path_shared):
        os.mkdir(path_shared)
        print("Folder %s created!" % path_shared)
    else:
        print("Folder %s already exists" % path_shared)

    if not os.path.exists(path_public):
        os.mkdir(path_public)
        print("Folder %s created!" % path_public)
    else:
        print("Folder %s already exists" % path_public)

    if not os.path.exists(path_log):
        os.mkdir(path_log)
        print("Folder %s created!" % path_log)
    else:
        print("Folder %s already exists" % path_log)

    if not os.path.exists(path_certs):
        os.mkdir(path_certs)
        print("Folder %s created!" % path_certs)
    else:
        try:
            files = os.listdir(path_certs)
            for file in files:
                file_path = os.path.join(path_certs, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print("All certs files deleted successfully.")
        except OSError:
            print("Error occurred while deleting certs files.")

    if not os.path.exists(path_current):
        os.mkdir(path_current)
        print("Folder %s created!" % path_current)
    else:
        try:
            shutil.rmtree(path_current)
            print("All current files deleted successfully.")
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

    return path_current
