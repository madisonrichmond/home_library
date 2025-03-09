from setuptools import setup, find_packages

setup(
    name="home_library",
    version="0.1",
    packages=find_packages(),
    install_requires=["click"],  # Dependencies
    entry_points={"console_scripts": ["home-library=home_library.cli:cli"]},
)
