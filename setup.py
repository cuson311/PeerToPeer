from setuptools import setup, find_packages
from codecs import open

# Get the long description from the relevant file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='p2pfs',
    version='0.1',
    description='Simple File System based on P2P concept',
    long_description=long_description,
    url='',
    author='hungvo2003vn',
    author_email='votanhung2003@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Networking',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='P2P, Networking',
    packages=find_packages(exclude=['tests']),
    install_requires=['coloredlogs', 'beautifultable', 'tqdm', 'aioconsole', 'msgpack',
                      'uvloop ; platform_system != "Windows"'],
    extras_require={
        'test': ['pytest', 'pytest-asyncio', 'pytest-cov', 'coverage'],
    },
    entry_points={
        'console_scripts': [
            'p2pfs=p2pfs.__main__:main',
        ],
    },
)
