"""Set required environment variables for GDAL, proj4 bundled with OSGeo4W.
 
We assume 'import numpy' imports the numpy package bundled with OSGeo4W, in order to find the OSGeo4W root path.
"""
 
import os
from pathlib import Path
 
import numpy as np

osgeo4w_root = str(Path(np.__file__).parents[5])
 
_envvars = {
    'GDAL_DATA': r'share\gdal',
    'GDAL_DRIVER_PATH': r'bin\gdalplugins',
    'GEOTIFF_CSV': r'share\epsg_csv',
    'PROJ_LIB': r'share\proj',
}
 
for var, rel_path in _envvars.items():
    os.environ[var] = os.path.join(osgeo4w_root, rel_path)
 
os.environ['PATH'] =  os.path.join(osgeo4w_root, 'bin') + ';' + os.environ['PATH']
os.add_dll_directory(os.path.join(osgeo4w_root, 'bin'))
