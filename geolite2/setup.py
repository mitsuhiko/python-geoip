import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__),
                       'VERSION')) as f:
    version = f.read().strip()


setup(
    name='python-geoip-geolite2',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version=version,
    url='http://github.com/mitsuhiko/python-geoip',
    packages=['_geoip_geolite2'],
    description='Provides access to the geolite2 database.  This product '
        'includes GeoLite2 data created by MaxMind, available from '
        'http://www.maxmind.com/',
    install_requires=['python-geoip'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
    ],
)
