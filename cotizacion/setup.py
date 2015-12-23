# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='cotizacion',
    version=version,
    description='Aplicacion de cotizacion EST',
    author='Lautaro Silva',
    author_email='jlsilva@init7.cl',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
