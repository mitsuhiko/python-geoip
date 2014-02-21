import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__),
                       'README')) as f:
    readme = f.read().strip()


setup(
    name='python-geoip',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version='1.2',
    url='http://github.com/mitsuhiko/python-geoip',
    long_description=readme,
    description='Provides GeoIP functionality for Python.',
    py_modules=['geoip'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
    ],
)
