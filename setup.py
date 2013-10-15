from setuptools import setup, find_packages
import os

version = '1.2'
shortdesc ="Interlude for Doctests provides an Interactive Console."
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read() 
longdesc += open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.rst')).read()

setup(name='interlude',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 6 - Mature',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
            'Topic :: Software Development :: Libraries :: Python Modules'        
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jens Klein',
      author_email='dev@bluedynamics.com',
      url='http://github.com/collective/interlude',
      license='LGPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
      ],
      extras_require={},
      entry_points="",
)
