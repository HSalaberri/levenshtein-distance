import setuptools

# Get project description from README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Establish setup parameters
setuptools.setup(name="levenshtein-distance",
                 version="1.0.0",
                 author="Haritz Salaberri",
                 author_email="hsalaberri@gmail.com",
                 description="Levenshtein distance calculator",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/HSalaberri/levenshtein-distance",
                 packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: License",
                              "Operating System :: OS Independent"],
                 python_requires='>=3.8.5')
