try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Puppet Catalog diff tool',
    'author': 'Xavier Morales',
    'url': 'https://github.com/xmorales/pcat_diff',
    'download_url': 'https://github.com/xmorales/pcat_diff',
    'author_email': '<xmorales.bcn@gmail.com>',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pcat_diff'],
    'scripts': [],
    'name': 'pcat_diff'
}

setup(**config)
