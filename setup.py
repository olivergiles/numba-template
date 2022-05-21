from setuptools import find_packages
from setuptools import setup
from setuptools import Extension
from src.my_module.haversine import cc

if __name__ == "__main__":
    setup(
        ext_modules=[cc.distutils_extension()],
    )
