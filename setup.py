#!/usr/bin/env python
import os
import shutil
import sys

from setuptools import find_packages, setup

VERSION = "0.0.5.1"

long_description = "Simple tools for logging and visualizing, loading and training"

setup_info = dict(
    # Metadata
    name="torchnet",
    version=VERSION,
    author="PyTorch",
    author_email="sergey.zagoruyko@enpc.fr",
    url="https://github.com/pytorch/tnt/",
    description="an abstraction to train neural networks",
    long_description=long_description,
    license="BSD",
    # Package info
    packages=find_packages(exclude=("test", "docs")),
    zip_safe=True,
    install_requires=["torch", "six", "future", "visdom"],
)

setup(**setup_info)
