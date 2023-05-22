"""Set required environment variables for GDAL, proj4 bundled with OSGeo4W.
 
We assume an environment where sys.base_prefix points to the Python interpreter in %OSGEO4W_ROOT%\apps\Pythonxy.
"""
 
import os
import sys
from pathlib import Path
 
python_root = sys.base_prefix
osgeo4w_root = str(Path(python_root).parents[1])

os.environ['OSGEO4W_ROOT'] = osgeo4w_root
_envvars = {
    'GDAL_DATA': os.path.join('share', 'gdal'),
    'GDAL_DRIVER_PATH': os.path.join('bin', 'gdalplugins'),
    'GEOTIFF_CSV': os.path.join('share','epsg_csv'),
    'PROJ_LIB': os.path.join('share','proj'),
}

for var, rel_path in _envvars.items():
    os.environ[var] = os.path.join(osgeo4w_root, rel_path)

sys.path.append(os.path.join(python_root, 'Scripts'))

os.environ['PATH'] = ';'.join([os.environ['PATH'],
                               os.path.join(osgeo4w_root, 'bin'),
                               os.path.join(python_root, 'Scripts')])

os.add_dll_directory(os.path.join(osgeo4w_root, 'bin'))
