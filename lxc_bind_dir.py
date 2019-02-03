#!/usr/bin/env python
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-n", "--name", dest="containerName", help="Container name argument.")
    parser.add_option("-s", "--source", dest="source", help="Relative path name where container will live.")
    parser.add_option("-p", "--path", dest="path", help="Path for directory on the container.")

    (options, arguments) = parser.parse_args()
    return options

def privilegedContainer(containerName, source, path):
    """
    This function will bind your dir in a container
    if the container is already crated.
    """
    #whoAmI = subprocess.call(["whoami"])
    #dir_source = "/home/$"+ whoAmI + "/.wm/" + containerName
    sourceArgs = "source=" + source
    pathArgs = "path=" + path

    subprocess.call(["lxc", "config", "set", containerName, "security.privileged", "true"])
    subprocess.call(["mkdir", source])
    subprocess.call(["lxc", "exec", containerName, "--", "mkdir", path])
    subprocess.call(["lxc", "config", "device", "add", containerName, "shareName", "disk", sourceArgs, pathArgs])

options = get_arguments()
privilegedContainer(options.containerName, options.source, options.path)
