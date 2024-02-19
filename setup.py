from distutils.core import setup
import py2exe, sys, os, shutil

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "main.py", "icon_resources": [(1, "data/logo.ico")], "dest_base" : "SaTEP"}],
    zipfile = None,
)

shutil.copytree('data', 'dist/data')