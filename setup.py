import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terminal-algebra-kaiferrall", # Replace with your own username
    version="0.0.1",
    author="Kai Ferrall",
    author_email="kaiferrall@gmail.com",
    description="Linear algebra CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaiferrall/linear-algebra-CLI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)