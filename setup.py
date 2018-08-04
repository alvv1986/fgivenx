#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def readme():
    with open('README.rst') as f:
        return f.read()


def get_version(short=False):
    with open('README.rst') as f:
        for line in f:
            if ':Version:' in line:
                ver = line.split(':')[2].strip()
                if short:
                    subver = ver.split('.')
                    return '%s.%s' % tuple(subver[:2])
                else:
                    return ver


setup(name='fgivenx',
      version=get_version(),
      description='fgivenx: Functional Posterior Plotter',
      long_description=readme(),
      author='Will Handley',
      author_email='wh260@cam.ac.uk',
      url='https://github.com/williamjameshandley/fgivenx',
      packages=['fgivenx', 'fgivenx.tests'],
      install_requires=['matplotlib', 'numpy', 'scipy'],
      extra_requires=['joblib', 'tqdm'],
      tests_require=['pytest', 'pytest-cov', 'coverage'],
      license='MIT',
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Astronomy',
                   'Topic :: Scientific/Engineering :: Physics',
                   'Topic :: Scientific/Engineering :: Visualization',
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   'Topic :: Scientific/Engineering :: Mathematics',
      ],
      )
