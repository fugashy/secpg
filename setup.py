from setuptools import setup, find_packages

def requirements_from_file(file_name):
    return open(file_name).read().splitlines()

setup(
    name='security_playground',
    version='0.0.0',
    packages=find_packages(),
    install_requires=requirements_from_file('requirements.txt'),
    entry_points={
        "console_scripts": [
            "secpg=security_playground.cli:main",
            ]
        },
)

