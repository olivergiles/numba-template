from setuptools import setup, Extension
from src.my_numba_package.haversine import cc

if __name__ == "__main__":
    with open("requirements.txt") as f:
        content = f.readlines()
    requirements = [x.strip() for x in content if "git+" not in x]

    setup(
        name="my_numba_package",
        version="0.0.0",
        description="Project Description",
        packages=["my_numba_package"],
        package_dir={"":"src"},
        install_requires=requirements,
        include_package_data=True,
        zip_safe=False,
        ext_modules=[cc.distutils_extension()],
    )
