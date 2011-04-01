#!/bin/bash
find . -name "*.pyc" -exec rm '{}' ';'
rm dist/depreciate.zip
rm dist/depreciate.tar.gz
mv src depreciate
tar -pczf dist/depreciate.tar.gz   --exclude=".*" --exclude="/.*" --exclude="/*/.*" --exclude="*.pyc" ./depreciate
mv depreciate/depreciate depreciate/depreciate.py
zip -r dist/depreciate.zip depreciate/[!\.]* -x \*/\.*
mv depreciate/depreciate.py depreciate/depreciate
mv depreciate src