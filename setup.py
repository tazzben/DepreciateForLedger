try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

long_desc = """
	This tool allows you to create a depreciation schedule appropriate for Ledger.
"""


setup(name="DepreciateForLedger",
      version=1.0,
      description="Depreciation tool for Ledger",
      author="Ben Smith",
      author_email="ben@wbpsystems.com",
      url="https://github.com/tazzben/DepreciateForLedger",
      license="MIT",
      packages=[],
      scripts=['depreciate'],
      package_dir={},
      long_description=long_desc,
      classifiers=[
          'Topic :: Text Processing',
          'Environment :: Console',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop'
      ]
     )