from setuptools import setup, find_packages

setup(
    name="goddard",
    version="1.0",
    packages=find_packages(),
    package_data={'goddard': ['resources/*']},
    zip_safe=False,
)
