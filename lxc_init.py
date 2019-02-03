#!/usr/bin/env python
import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-n", "--name", dest="name", help="Type in the name of the container.")
    parser.add_option("-s", "--source", dest="source", help="Local directory for container to keep his files.")
    parser.add_option("-p", "--path", dest="path", help="Working directory to by bind with local directory.")

    (options, arguments) = parser.parse_args()
    return options

def launch_container(containerName, source, path):
    """
    This function create a lxc container.
    """
    sourceArgs = "source=" + source
    pathArgs = "path=" + path

    subprocess.call(["lxc", "launch", "images:debian/9/amd64", containerName])
    subprocess.call(["lxc", "config", "set", containerName, "security.privileged", "true"])
    subprocess.call(["mkdir", containerName])
    subprocess.call(["lxc", "exec", containerName, "--", "mkdir", containerName])
    subprocess.call(["lxc", "config", "device", "add", containerName, "shareName", "disk", sourceArgs, pathArgs])


options = get_args()

launch_container(options.name, options.source, options.path)
