from codecs import open
from os import path
from glob import glob
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') \
        as f: long_description = f.read()

setup(name='miniworldmaker',
      version='0.9.41',
      description='Create 2D Miniworlds and Games',
      long_description=long_description,
      long_description_content_type='text/markdown',
      keywords=['games', 'education', 'mini-worlds'],  # arbitrary keywords
      author='Andreas Siebel',
      author_email='andreas.siebel@it-teaching.de',
      url='https://github.com/asbl/miniworldmaker',
      download_url='https://github.com/asbl/miniworldmaker',
      license="OSI Approved :: MIT License",
      classifiers=["License :: OSI Approved :: MIT License",
                   "Programming Language :: Python",
                   "Development Status :: 4 - Beta",
                   "Intended Audience :: Education",
                   "Topic :: Education",
                   ],
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
      package_dir={'miniworldmaker': 'miniworldmaker'},
      install_requires=['pygame'],
      include_package_data=True,
      )
