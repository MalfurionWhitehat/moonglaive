from setuptools import setup

setup(
    name='moonglaive',
    version='0.0.1',
    description='Three-bladed weapon of the night elf Sentinels',
    url='https://github.com/MalfurionWhitehat/moonglaive',
    author='MalfurionWhitehat',
    author_email='MalfurionWhitehat@proton.me',
    license='MIT',
    packages=['moonglaive'],
    install_requires=[
        'typing',
        'datetime',
        'python-dateutil',
        'python-Levenshtein',
        'fuzzywuzzy',
        'requests',
        'argparse',
        'tabulate'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
