#!/usr/bin/python3

"""Fabric Script (based on the file 2-do_deploy_web_static.py) that
creates and distributes an archive to your web servers,
using the function deploy"""

import os
from datetime import datetime
from fabric.api import local
from fabric.api import env
from fabric.api import run
from fabric.api import put

env.hosts = ["web-01.emyjakarta.tech", "web-02.emyjakarta.tech"]
env.user = "ubuntu"
# env.key_filename = "~/.ssh/alx-server-key.pem"
env.key_filename = "~/.ssh/my_servers"


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{date}.tgz"
    if os.path.exists("web_static") is False:
        return None

    local(f"tar -cvzf {file_path} web_static")
    local(f"chmod 664 {file_path}")  # Set the permissions to rw-rw-r--
    return file_path


def do_deploy(archive_path: str) -> bool:
    """Distributes an archive to your web servers.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    if not archive_path:
        return False

    if os.path.exists(archive_path) is False:
        return False

    archive_name = archive_path.split("/")[-1]
    archive_name_no_ext = archive_name.split(".")[0]

    put(archive_path, "/tmp/")
    run(f"mkdir -p /data/web_static/releases/{archive_name_no_ext}/")
    run(
        f"tar -xzf /tmp/{archive_name} -C "
        f"/data/web_static/releases/{archive_name_no_ext}/"
    )
    run(f"rm /tmp/{archive_name}")
    # Extracted folder name
    extracted_folder = (
            f"/data/web_static/releases/{archive_name_no_ext}/web_static"
    )

    # Move files from extracted folder to current
    run(
        f"mv {extracted_folder}/* "
        f"/data/web_static/releases/{archive_name_no_ext}/"
    )

    # Cleanup extracted folder
    run(f"rm -rf {extracted_folder}")

    # run(
    #    f"mv /data/web_static/releases/{archive_name_no_ext}/web_static/* "
    #    f"/data/web_static/releases/{archive_name_no_ext}/"
    # )
    # run(f"rm -rf /data/web_static/releases/{archive_name_no_ext}/web_static")
    # run("rm -rf /data/web_static/current")
    run(
        f"ln -s /data/web_static/releases/{archive_name_no_ext}/ "
        "/data/web_static/current"
    )

    print("New version deployed!")
    return True


def deploy():
    """Creates and distributes an archive to your web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
