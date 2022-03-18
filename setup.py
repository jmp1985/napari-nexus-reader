#
# Copyright (C) 2019 James Parkhurst
#
# This code is distributed under the BSD license.
#
from setuptools import setup


def main():
    """
    Setup the package

    """
    setup(
        packages=["src/napari_nexus_reader"],
        install_requires=[],
        setup_requires=["pytest-runner"],
        tests_require=["pytest", "pytest-cov", "mock"],
        test_suite="tests",
    )


if __name__ == "__main__":
    main()
