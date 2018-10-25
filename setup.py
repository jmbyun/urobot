import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="urobot",
    version="0.0.1",
    author="Jeongmin Byun",
    author_email="jmbyun91@gmail.com",
    description="Environment for controlling a robot on the grid world for learning to program in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/jmbyun/urobots",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        'tornado',
    ]
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
