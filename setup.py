import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pedalpi-blog",
    version="0.0.1",
    #author="Example Author",
    #author_email="author@example.com",
    description="Pedal Pi - blog",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pedalpi/blog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pelican=4.2.0',
        'markdown'
    ],
)