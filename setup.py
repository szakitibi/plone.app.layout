from setuptools import find_packages
from setuptools import setup


version = "4.0.0a12.dev0"

long_description = open("README.rst").read() + "\n" + open("CHANGES.rst").read()

setup(
    name="plone.app.layout",
    version=version,
    description="Layout mechanisms for Plone",
    long_description=long_description,
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="plone layout viewlet",
    author="Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://pypi.org/project/plone.app.layout",
    license="GPL version 2",
    packages=find_packages(),
    namespace_packages=["plone", "plone.app"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Acquisition",
        "DateTime",
        "plone.app.content",
        "plone.app.viewletmanager >=1.2",
        "plone.base",
        "plone.batching >1.0.999",
        "plone.i18n",
        "plone.memoize",
        "plone.portlets",
        "plone.registry",
        "Products.CMFCore",
        "Products.CMFDynamicViewFTI",
        "Products.CMFEditions >=1.2.2",
        "setuptools",
        "zope.component",
        "zope.deferredimport",
        "zope.deprecation",
        "zope.dottedname",
        "zope.i18n",
        "zope.interface",
        "zope.publisher",
        "zope.schema",
        "zope.viewlet",
        "Zope",
    ],
    extras_require=dict(
        test=[
            "plone.app.contenttypes",
            "plone.app.intid",
            "plone.app.relationfield",
            "plone.app.testing",
            "plone.dexterity",
            "plone.locking",
            "plone.testing",
            "z3c.relationfield",
            "zope.annotation",
        ]
    ),
)
