from setuptools import setup

setup(name='Bowling',
      version='1.0',
      description='Python module to count bowling scores',
      author='Zaytsev Dmitriy',
      license="BSD",
      author_email='gward@python.net',
      packages=['bowling', 'bowling.tests'])


# python setup.py sdist bdist_wheel
# python setup.py bdist_egg

