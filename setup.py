import setuptools

with open(
        "../../../../Google Drive/Curso 3º GII/1er Cuatrimestre_/OH - Optimización Heurística/Practica/groupDaniAaron/README.md",
        "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="groupXX",  # Replace with your own username
    version="1.0.0",
    author="GroupXX",
    author_email="author@example.com",
    description="Heuristic optimization 1st practical work, by Group XX.",
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
