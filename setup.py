from setuptools import setup, find_packages

NAME = "likeinsta"
VERSION = "0.1.0"

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name=NAME,
    version=VERSION,
    description="Likes for instagram with selenium",
    author="Jeremy Silva",
    author_email="jeremysilvasilva@gmail.com",
    url="",
    keywords=["instagram", "likes","likes_instagram"],
    install_requires=required,
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.5',
    long_description="""\
    Likes for instagram with selenium
    """
)