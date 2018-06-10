#!/usr/bin/env python

import os
import sys
from distutils.sysconfig import get_python_lib
from setuptools import find_packages, setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3,4)

if CURRENT_PYTHON < REQUIRED_PYTHON:
	sys.stderr.write("""
		============================
		Python Version not supported
		============================

		Your python version is {}.{} and
		required version is {}.{} .

		""".format(*(CURRENT_PYTHON + REQUIRED_PYTHON)))
	sys.exit(1)


def read(fname):
	with open(os.path.join(os.path.dirname(__file__), fname)) as f:
		return f.read()


setup(name="Anonymous Email",
	  version="1.0",
	  description="Python Script to send e-mail with Anonymous Sender",
	  author="Umesh Joshi",
	  long_description=read('README.md'),
	  author_email="umesh14el007@gmail.com",
	  packages=['MechanicalSoup'],
	  )