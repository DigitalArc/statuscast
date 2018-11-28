import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="statuscast",
    version="0.0.1",
    author="DigitalArc",
    author_email="contact@thedigitalarc.com",
    license='MIT',
    keywords='pretty print status modern simple',
    description="Cast status of a script with a nice simple look.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DigitalArc/statuscast",
    packages=setuptools.find_packages(),
    install_requires=['colorama'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
