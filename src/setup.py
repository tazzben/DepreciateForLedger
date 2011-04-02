from distutils.core import setup
import py2exe
from glob import glob

data_files = [("Microsoft.VC90.CRT", glob(r'c:\dist\*.*'))]

setup(data_files=data_files,console=['depreciate.py'])