# QGS Tools

Scripts and Python modules for QGIS plugin development.

## Overview

### qgis_env_helper

A windows (OSGeo4W) QGIS installation can be moved to any directory and will keep working, as long as the paths in the
environment variables defined in the various `.env` files in the `bin` subdirectory (e.g. `bin/qgis-bin.env`) are 
adjusted.  You can update the `.env` files automatically by putting the scripts `update_qgis_env.bat` and
`update_qgis_env.py` in the QGIS root directory and running the bat script.

### sitecustomize.py

If you are developing in a virtual env based on your QGIS Python environment (created using
`python -m virtualenv --system-site-packages [...]`), you need to set a few environment variables in order to get GDAL
etc to work.  Putting this sitecustomize.py script in your virtualenv's site-pacakages directory should take care of
that automatically. 

### src/marvin_qgis_tools

A python package for code that can be used in various QGIS plugins.
