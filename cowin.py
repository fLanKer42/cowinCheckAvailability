# GET https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=233&date=2-06-2021

from datetime import datetime, timedelta
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

num_days = 1
district_id = 233
x = datetime.today() + timedelta(days=num_days)

Url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=' + str(district_id) + '&date=' + str(x.strftime("%d")) + '-' + str(x.strftime("%m")) + '-' + str(x.strftime("%Y"))

jhand = open("vaccine.json", "w")

fhand = urllib.request.urlopen(Url, context=ctx)
for line in fhand:
    jhand.write(line.decode().strip())
jhand.close()
fhand.close()

