import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ahapy",
    version="0.0.3",
    author="Robert Henkhaus",
    author_email="rhenkhaus@gmail.com",
    description="A small Aha.io API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/henkhaus/ahapy",
    project_urls={
        "Bug Tracker": "https://github.com/henkhaus/ahapy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["aha", "aha.io"],
    packages="ahapy",
    package_dir={'ahapy': 'ahapy'},
    python_requires=">=3.6",
)