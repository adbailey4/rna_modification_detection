#!/usr/bin/env python

import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(
            join(dirname(__file__), *names),
            encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='rna_modification_detection',
    version='0.0.1',
    license='MIT License',
    description='Detect rna modifications using a neural network.',
    author='Andrew Bailey, Shreya Mantripragada, Alejandra Duran, Abhay Padiyar',
    author_email='bailey.andrew4@gmail.com',
    url='https://github.com/adbailey4/rna_modification_detection',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    project_urls={
        'Issue Tracker': 'https://github.com/adbailey4/rna_modification_detection/issues',
    },
    keywords=['variant', 'modification', 'neural network'],
    python_requires='>=3.5',
    install_requires=[
        'pandas>=1.0.5',
        'numpy>=1.14.2',
        'matplotlib>=3.2.2'],
    setup_requires=['Cython>=0.29.21']
)
