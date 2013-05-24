from setuptools import setup, find_packages
import os

version = '0.001'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='anon.vtv',
      version=version,
      description="Un paquete python",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='@hbastidas',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['anon'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pygame'
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts':
              ['vtv = anon.vtv.main:main']
              },
      )