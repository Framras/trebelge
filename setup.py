# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

# get version from __version__ variable in trebelge/__init__.py
from trebelge import __version__ as version

setup(
    name='trebelge',
    version=version,
    description='TR Revenue Administration eBelge integration of e-invoice, e-waybill, etc for ErpNext',
    author='Framras AS-Izmir',
    author_email='bilgi@framras.com.tr',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
