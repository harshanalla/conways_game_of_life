from setuptools import setup
from setuptools import find_packages

setup(
    name='conways_game_of_life',
    version='1.0.0',
    url='',
    license='',
    author='Harsha',
    author_email='sriharsha.nalla@outlook.com',
    description='Implementation of Conway\'s game of life, written in python',
    packages=find_packages(exclude=('tests*', 'Tests*')),
    install_requires = [''],
    entry_points={
        'console_scripts': [
            'game-of-life = game.handler:entry',
        ]
    }
)
