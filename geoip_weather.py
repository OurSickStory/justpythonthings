import requests
import json
from win10toast import ToastNotifier


ipstack_key = 'ipstackkeyhere'
ipstack_base = 'http://api.ipstack.com/check?access_key='
tail = '&output=json'
ipurl = ipstack_base + ipstack_key + tail
response = requests.get(ipurl)
ipdata = response.json()
ipjson_str = json.dumps(ipdata)
ipresp_dict = json.loads(ipjson_str)
lat = ipresp_dict['latitude']
long = ipresp_dict['longitude']
city = 'lat=' + str(lat) + '&lon=' + str(long)
key = 'owmkeyhere'
base = 'http://api.openweathermap.org/data/2.5/weather?'
id = '&appid='
url = base + city + id + key
response = requests.get(url)
data = response.json()
json_str = json.dumps(data)
resp_dict = json.loads(json_str)
temp = resp_dict['main']['temp']
loc = resp_dict['name']
k = int(temp)
kelvtemp = (k - 273) * 1.8 + 32
toaster = ToastNotifier()
toaster.show_toast('The current temp in {} is {}'.format(loc, int(kelvtemp)),
                   duration=10)

