#!/bin/sh

cd _geoip_geolite2
rm *.mmdb
wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz
gunzip "GeoLite2-City.mmdb.gz"
cd ..

export PYTHONPATH=`pwd`:`pwd`/..
python -c "if 1:
    from geoip import geolite2;
    info = geolite2.get_info()
    print info.date.strftime('%Y.%m%d')
" > VERSION
