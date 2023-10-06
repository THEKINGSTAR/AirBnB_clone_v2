#!/usr/bin/python3
"""
1. Compress before sending
Fabric script that generates a .tgz
archive from the contents of the web_static folder
"""


from fabric.operations import local


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static
    """
    source_path = "web_static"
    target_path = "versions/web_static_$(date '+%Y%m%d%H%M%S').tgz"

    local("mkdir -p versions")
    local(f"tar -cvzf {target_path} {source_path}")

    if local(f"test -e {target_path}").return_code == 0:
        return target_path
    else:
        return None
