import os
from pathlib import Path
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = (Path(__file__).resolve().parent / 'version.txt').read_text().strip()

long_description = (
    read('README.rst')
    + '\n' +
    read('CHANGES.rst')
    + '\n'
    )

setup(name='plone.caching',
      version=version,
      description="Zope 2 integration for z3c.caching",
      long_description=long_description,
      # Get more strings from
      # https://pypi.org/classifiers/
      classifiers=[
         "Development Status :: 5 - Production/Stable",
          "Framework :: Plone",
          "Framework :: Plone :: 5.0",
          "Framework :: Plone :: 5.1",
          "Framework :: Plone :: 5.2",
          "Framework :: Plone :: Core",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      keywords='plone http caching',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='https://pypi.org/project/plone.caching',
      license='GPL',
      packages=find_packages(),

      include_package_data=True,
      python_requires='>=3.10',
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.caching [zcml]',
          'plone.registry',
          'zope.interface',
          'zope.component',
          'zope.i18nmessageid',
          'zope.schema',
          'plone.transformchain',
          'Zope>=6.1,<7',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
