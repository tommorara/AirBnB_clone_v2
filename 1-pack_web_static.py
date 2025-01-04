#!/usr/bin/python3

"""A Fabric Script that generates a .tgz archive from the contents of the
web_static folder of the AirBnB Clone repo using the function do_pack"""

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"versions/web_static_{date}.tgz"

    # Print the packing message
    print(f"Packing web_static to {file_path}")

    if os.path.exists('web_static') is False:
        return None

    local(f"tar -cvzf {file_path} web_static")
    local(f"chmod 664 {file_path}")  # Set the permissions to rw-rw-r--

    # Get the size of the generated archive
    archive_size = os.path.getsize(file_path)

    # Print the packed message with the file size
    print(f"web_static packed: {file_path} -> {archive_size}Bytes")

    return file_path
