"""
Adapted from https://github.com/pypa/sampleproject/blob/master/setup.py
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import re
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

descr = "Python library for loading/cleaning data used in qeds training"

# get the version from the version.py file
with open(path.join(here, "qeds", "version.py"), encoding="utf-8") as f:
    contents = f.read()
    version = re.match(r'__version__ = "(.+)"', contents).group(1)

setup(
    name="qeds",

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description=descr,
    long_description=long_description,

    # The project"s main homepage.
    url="https://github.com/QuantEcon/qeds",
    # url="https://github.com/sglyon/uscensus",

    # Author details
    author="qeds Data",
    author_email="admin@qedsdata.com",

    # Choose your license
    license="BSD-3",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",

        # Indicate who your project is intended for
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Database :: Front-Ends",
        "Topic :: Education",

        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: BSD License",

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6"
    ],

    # What does your project relate to?
    keywords="data pandas economics census education",

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=["contrib", "docs", "tests"]),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip"s
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["pandas", "requests", "quandl", "scipy", "numpy", "quantecon",
                      "matplotlib", "pyarrow", "openpyxl", "plotly",
                      "pandas_datareader", "scikit-learn", "seaborn",
                      "statsmodels"],
)
