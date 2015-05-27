import os
import argparse
from setuptools import setup

setup(
    name="MyFlasky",
    version="1.0dev",
    py_modules=["hello_flask", "request"],
    install_requires=[
        "flask",
        "flask-script"
    ],
    entry_points="""
        [console_scripts]
        hello-flask=hello_flask:main
        request=request:main
        """
)
