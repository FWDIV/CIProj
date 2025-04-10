from setuptools import setup, find_packages
"""_summary_
    packaging the src folder
"""
setup(
    name="ciproject",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"":"src"}
)