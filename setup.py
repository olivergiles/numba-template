from setuptools import find_packages, setup, Extension
from src.my_numba_package.haversine import cc

if __name__ == "__main__":
    with open("requirements.txt") as f:
        content = f.readlines()
    requirements = [x.strip() for x in content if "git+" not in x]

    setup(
        name="haversine_vectorize",
        version="1.0",
        description="Project Description",
        packages=find_packages(),
        install_requires=requirements,
        include_package_data=True,
        zip_safe=False,
        ext_modules=[cc.distutils_extension()],
    )
