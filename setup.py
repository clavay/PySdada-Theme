# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
from pyscada import theme as plugin


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Environment :: Console',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Operating System :: POSIX',
    'Operating System :: MacOS :: MacOS X',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Scientific/Engineering :: Visualization'
]
setup(
    author=plugin.__author__,
    author_email="clavayssiere@univ-pau.fr",
    name="pyscada-" + plugin.plugin_name_lower,
    version=plugin.__version__,
    description=plugin.plugin_name
    + " extension for PyScada a Python and Django based Open Source SCADA System",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    url="http://www.github.com/pyscada/PyScada",
    license="AGPLv3",
    platforms=["OS Independent"],
    classifiers=CLASSIFIERS,
    install_requires=[
        "pyscada>=0.8.0",
    ],
    packages=find_packages(exclude=["project", "project.*"]),
    include_package_data=True,
    zip_safe=False,
    test_suite="runtests.main",
    namespace_packages=["pyscada"],
)
