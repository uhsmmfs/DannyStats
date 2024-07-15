from setuptools import setup

setup(
    name='DannyStats',
    description='Non-violent Stats',
    version="1.0.0",

    url='https://github.com/uhsmmfs/DannyStats',
    author='UHS Math Modeling for Society',
    author_email='UHSMMforS@gmail.com',
    license='MIT',
    
    install_requires=[
        'scipy',
    ],
    packages=['dannystats'],
)