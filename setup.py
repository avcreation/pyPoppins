from setuptools import setup, find_packages

open('MANIFEST.in', 'w').write('\n'.join((
    "include *.md",
)))

from poppinsbag import __version__

setup(

    name="poppinsbag",
    version=__version__,
    packages=find_packages('.'),
    author="zArglex",
    author_email="dev@avcreation.fr",
    description="Another set of tools for python",
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=['pyOpenSSL'],
    classifiers=[
        'Programming Language :: Python',
        "Intended Audience :: Information Technology",
        "License :: MIT",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.4"
    ],
    url="https://github.com/avcreation/pyPoppins"
)


