import setuptools

with open(
        "README.txt","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="group14",  # Replace with your own username
    version="2.2.0",
    author="Group14",
    author_email="author@example.com",
    description="Heuristic optimization 2.2 practical work, by Group 14.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
