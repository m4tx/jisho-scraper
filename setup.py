from codecs import open
from os import path

import setuptools
from setuptools import setup

base_path = path.abspath(path.dirname(__file__))

with open(path.join(base_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jisho_scraper',
    version='1.0.0',
    description='Jisho scraper capable of outputting search results to CSV or Anki',
    long_description=long_description,
    url='https://github.com/m4tx/jisho-scraper',

    author='Mateusz Maćkowski',
    author_email='mateusz@mackowski.org',
    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Education',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    keywords='jisho anki hiragana katakana kanji',
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.25.1,<3'],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'jisho-scraper=jisho_scraper.main:main',
        ],
    },
)
