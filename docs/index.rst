python-geoip
============

.. module:: geoip

python-geoip is a library that provides access to GeoIP databases.
Currently it only supports accessing MaxMind databases.  It's similar to
other GeoIP libraries but comes under the very liberal BSD license and
also provides an extra library that optionally ships a recent version of
the Geolite2 database as provided by MaxMind.

The ``python-geoip-geolite2`` package includes GeoLite2 data created by
MaxMind, available from `maxmind.com <http://www.maxmind.com>`_ under
the Creative Commons Attribution-ShareAlike 3.0 Unported License.

Installation
------------

You can get the library directly from PyPI::

    pip install python-geoip

If you also want the free MaxMind Geolite2 database you can in addition::

    pip install python-geoip-geolite2

Usage
-----

If you have installed the ``python-geoip-geolite2`` package you can start
using the GeoIP database right away::

    >>> from geoip import geolite2
    >>> match = geolite2.lookup('17.0.0.1')
    >>> match is not None
    True
    >>> match.country
    'US'
    >>> match.continent
    'NA'
    >>> match.timezone
    'America/Los_Angeles'
    >>> match.subdivisions
    frozenset(['CA'])

If you want to use your own MaxMind database (for instance because you
paid for the commercial version) you can open the database yourself::

    >>> from geoip import open_database
    >>> db = open_database('path/to/my.mmdb')

API
---

.. autofunction:: open_database

.. autodata:: geolite2

.. autoclass:: Database
   :members:

.. autoclass:: IPInfo
   :members:

.. autoclass:: DatabaseInfo()
   :members:
