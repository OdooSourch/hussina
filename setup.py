from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in husainia/__init__.py
from husainia import __version__ as version

setup(
	name="husainia",
	version=version,
	description="Husainia Api",
	author="Smb ",
	author_email="bhaveshodedara00@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
