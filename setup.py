from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
	readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert=>5", "requests>=2"]

setup(
	name="backend",
	version="0.0.1",
	author="Mateusz Gruszka",
	author_email="gruszka.mateusz87@gmail.om",
	description="Program analizujący dane z GUS",
	long_description=readme,
	url="https://github.com/GMT-Mati/analitykGUS",
	packages=find_packages(),
	install_requires=requirements,
	classifires=[
		"Programming Language :: Python :: 3.7",
		"Licence :: OSI Approved :: GNU General Public License v3.0",
	],
)


