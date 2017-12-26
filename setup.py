from setuptools import setup

import os
os.system('pip install hg+https://bitbucket.org/saurabhy/hermes')

setup(name='functionoptimizer',
      version='0.1.0',
      description='Optimization library for functions. It aggregates available optimisations tools.',
      url='https://github.com/ML-Guy/functionoptimizer',
      install_requires=[
          'six',
          'numba',],
      packages=['functionoptimizer'],
      zip_safe=False)
