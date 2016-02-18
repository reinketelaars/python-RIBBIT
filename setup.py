from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

requirements = [
    req.strip() for req
    in open('requirements.txt').readlines() if not req.startswith('#')]


setup(name='python-RIBBIT',
      version='1.0.0',
      description='frog.tips RIBBIT client',
      long_description=long_description,
      classifiers=[],
      keywords='FROG RIBBIT CROAK',
      author='Gabriel Gironda',
      author_email='gabriel@gironda.org',
      url='https://github.com/gabrielg/python-RIBBIT',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
      extras_require={
          'test': [
              'pytest',
              'vcrpy',
          ]
      },
      entry_points="""
      [console_scripts]
      RIBBIT=RIBBIT.scripts.cli:cli
      """
      )
