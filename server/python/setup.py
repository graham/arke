import setuptools
from setuptools import setup, find_packages, Extension, Feature

setup(
        name="arke",
        version=0.3,
        description="Arke API framework.",
        long_description="Arke API Framework.",
        author="Graham Abbott",
        author_email="graham.abbott@gmail.com",
        packages=find_packages(),
        platforms=['any'],
        zip_safe=True,
    )

