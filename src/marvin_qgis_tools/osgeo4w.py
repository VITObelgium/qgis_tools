# Copyright (2022) VITO NV.
"""Functions to interact with the OSGeo4W installer."""

import importlib
import subprocess
import threading
import os
import time

from PyQt5.QtWidgets import QMessageBox
from qgis.utils import iface


class ExitTask(threading.Thread):
    """Background task to exit QGIS.

    We can only run iface.actionExit().trigger() after QGIS initialization is complete => use a background task to
    wait for that, in case we are running before/during QGIS initialization."""
    def run(self, *args, **kwargs):
        while True:
            iface.actionExit().trigger()
            time.sleep(0.5)


def check_packages(packages):
    """Check if required packages are available, otherwise run osgeo4w-setup to install them, and exit QGIS.

    :param packages: dictionary of {python_package: osgeo4w_package}, e.g. {'rasterio': 'python3-rasterio'}
    :return: True if all required packages are available.
    """
    try:
        for python_package in packages:
            importlib.import_module(python_package)
        # If all imports succeed: return True
        return True
    except ModuleNotFoundError:
        osgeo_root = os.getenv('OSGEO4W_ROOT')
        if osgeo_root is None:
            # We are on linux, mac, or a non-OSGeo4W QGIS version (unlikely): user should take care of dependencies.
            QMessageBox.warning(None, 'Plugin Installation',
                                'Some dependencies are not available.  Please make sure the QGIS python '
                                'environment has access to the following packages: ' +
                                ', '.join(packages))
        else:  # We are on OSGeo4W -> run the installer
            answer = QMessageBox.question(None, 'Plugin Installation',
                                          'We need to install a few extra packages.  Click OK to start the OSGeo4W '
                                          'installer and exit QGIS.  Click Cancel to abort the plugin installation.',
                                          QMessageBox.Ok | QMessageBox.Cancel)
            if answer == QMessageBox.Ok:
                # Run osgeo4w-setup and exit QGIS:
                args = [f'{osgeo_root}\\bin\\osgeo4w-setup.exe', '--advanced', '--autoaccept']
                # add required packages to list of installer arguments:
                for osgeo4w_pkg in packages.values():
                    args.append('--packages')
                    args.append(osgeo4w_pkg)
                subprocess.Popen(args)
                # Exit QGIS in case setup needs to update files which are in use (e.g. the qgis executable, GDAL, ...)
                ExitTask().start()
        return False
