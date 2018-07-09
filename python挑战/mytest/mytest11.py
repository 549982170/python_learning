# encoding:utf-8
# usr/bin/python
import json
from geopy.geocoders import Nominatim


# 使用geopy查询
def geocodeN(address):
    gps = Nominatim()
    location = gps.geocode(address)
    return location.longitude, location.latitude


print geocodeN("深圳")

def change_unicode_to_chinese_str(string):
    try:
        new_string = string.decode('unicode_escape').encode("utf-8")
    except:
        new_string = str(string)
    finally:
        return new_string

a = {"a": "深圳"}

b = json.dumps(a)
print b

c = json.loads(b)
print c["a"]
print change_unicode_to_chinese_str(c["a"])