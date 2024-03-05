import PyInstaller.__main__
import shutil

PyInstaller.__main__.run([
    '--clean',
    '-n SaTEP',
    'main.py',
    '--onefile',
    '--windowed',
    '--icon=data/logo.ico',
    '--upx-dir=upx-4.2.2-win64'
])

shutil.copytree('data', 'dist/data')