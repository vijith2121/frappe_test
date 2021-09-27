from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in test_site/__init__.py
from test_site import __version__ as version

setup(
	name="test_site",
	version=version,
	description="registration",
	author="vahini@",
	author_email="vahini@12.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
