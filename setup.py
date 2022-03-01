from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in horti_management/__init__.py
from horti_management import __version__ as version

setup(
	name="horti_management",
	version=version,
	description="app for horti",
	author="Aman",
	author_email="amanuelg@360ground.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
