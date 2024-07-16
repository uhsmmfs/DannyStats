from setuptools import setup, find_packages

setup(
    name='DannyStats',
    description='Nonviolent Stats',
    version="1.0.0",

    url='https://github.com/uhsmmfs/DannyStats',
    author='UHS Math Modeling for Society',
    author_email='UHSMMforS@gmail.com',
    license='MIT',

    install_requires=[
        'scipy',
        'numpy',
        'matplotlib',
    ],
    packages=find_packages(exclude=['tests']),
)
