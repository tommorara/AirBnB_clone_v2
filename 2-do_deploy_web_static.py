#!/usr/bin/python3

"""Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy"""

import os
from datetime import datetime
from fabric.api import local
from fabric.api import env
from fabric.api import run
from fabric.api import put
from fabric.api import sudo

env.hosts = [
    "web-01.emyjakarta.tech",
    "web-02.emyjakarta.tech",
    "172.29.212.149"]
env.roledefs = {
    'remote_servers': ['web-01.emyjakarta.tech', 'web-02.emyjakarta.tech'],
    'local_server': ['172.29.212.149']
}
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def set_user():
    """Sets the appropriate user for each host."""
    if env.host_string == '172.29.212.149':
        env.user = 'emyjakarta273'
    else:
        env.user = 'ubuntu'


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
    # if not archive_path:
    #    return False
    if not archive_path or not os.path.exists(archive_path):
        print("Archive path is invalid or does not exist")
        return False

    try:

        # if os.path.exists(archive_path) is False:
        #    return False

        set_user()
        archive_name = archive_path.split("/")[-1]
        archive_name_no_ext = archive_name.split(".")[0]

        print(f"Deploying {archive_name} to servers...")

        put(archive_path, "/tmp/")

        if env.host == "172.29.212.149":
            local(
                f"sudo mkdir -p /data/web_static/releases/"
                f"{archive_name_no_ext}/"
            )
            local(
                f"sudo tar -xzf /tmp/{archive_name} -C "
                f"/data/web_static/releases/{archive_name_no_ext}/"
            )
            local(f"sudo rm /tmp/{archive_name}")
            local(
                f"sudo mv /data/web_static/releases/"
                f"{archive_name_no_ext}/web_static/* "
                f"/data/web_static/releases/{archive_name_no_ext}/ || true"
            )
            local(
                f"sudo rm -rf /data/web_static/releases/"
                f"{archive_name_no_ext}/web_static"
            )
            local("sudo rm -rf /data/web_static/current || true")
            local(
                f"sudo ln -s /data/web_static/releases/"
                f"{archive_name_no_ext}/ /data/web_static/current"
            )
        else:
            sudo(f"mkdir -p /data/web_static/releases/{archive_name_no_ext}/")
            sudo(
                f"tar -xzf /tmp/{archive_name} -C "
                f"/data/web_static/releases/{archive_name_no_ext}/"
            )
            sudo(f"rm /tmp/{archive_name}")

            # Remove existing directories
            # run(f"rm -rf /data/web_static/releases/
            # {archive_name_no_ext}/web_static")

            # Move extracted files (including wildcards to handle empty
            # directories)
            sudo(
                f"mv /data/web_static/releases/"
                f"{archive_name_no_ext}/web_static/* "
                f"/data/web_static/releases/{archive_name_no_ext}/ || true"
            )

            # Remove empty directories after move
            sudo(
                f"rm -rf /data/web_static/releases/"
                f"{archive_name_no_ext}/web_static"
            )

            # Remove old symbolic link
            sudo("rm -rf /data/web_static/current || true")

            # Create new symbolic link
            sudo(
                f"ln -s /data/web_static/releases/{archive_name_no_ext}/ "
                "/data/web_static/current"
            )

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
