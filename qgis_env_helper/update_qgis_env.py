"""Update the OSGeo4W root directory in directory paths specified in qgis .env files.

This script should be placed in the root directory of the OSGeo4W installation, and should be run from the batch script
update_qgis_env.bat, which will provide the windows short name of the root directory.
"""
import glob
import os
import sys


def update_env_file(env_file, new_root):
    with open(env_file, 'rt') as f:
        qgis_env = f.read()

    # Find the QGIS path used in the existing env file by looking for the OSGEO4W_ROOT variable:
    env_var = 'OSGEO4W_ROOT='
    start = qgis_env.find(env_var) + len(env_var)
    end = qgis_env.find('\n', start)
    old_root = qgis_env[start:end]

    # Replace the OSGeo4W root in every environment variable.  For some variables, directories are separated by
    # backslashes, for others, we have to use forward slashes.
    # make strings for new and old OSGeo4W root directories, with forward slashes:
    new_root_fwd = new_root.replace('\\', '/')
    old_root_fwd = old_root.replace('\\', '/')
    # replace old root with backslashes by new root with backslash, old root with fwd slash by new root with fwd slash:
    with open(env_file, 'wt') as f:
        f.write(qgis_env.replace(old_root, new_root).replace(old_root_fwd, new_root_fwd))
    # Create a backup of the original qgis env file.
    with open(env_file + '_original', 'wt') as f:
        f.write(qgis_env)


def main():
    # Basic checks:
    if not len(sys.argv) == 2 or not os.path.isdir(sys.argv[1]):
        print('ERROR: Provide the windows short name of the OSGeo4W installation root as a command line argument.')
        sys.exit(1)
    new_root = sys.argv[1].rstrip('\\')

    for env_file in glob.glob(os.path.join(new_root, 'bin', '*.env')):
        update_env_file(env_file, new_root)


if __name__ == '__main__':
    main()
