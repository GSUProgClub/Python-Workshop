'''
libraries in pyton:
This workshop will show how to use the requests library in python.
This library is used for making web requests to apis.
This is a simple way to get info from apis.

-pip
This is the commandline tool to install libraries to python.
If it is not already installed to to https://bootstrap.pypa.io/get-pip.py and download and run the pyton file.
pip should be pip or pip3 in the terminal (varies based on install method)


-import 
import is the keyword for using libraries in python
'''

import requests

'''
If you wanto to know more: https://www.w3schools.com/tags/ref_httpmethods.asp

GET is the main method used to get information from an api.
'''

responce = requests.get('http://wttr.in/')
# this will just print the reponce object not the infor in the responce. Here it is the responce code of 200 a sucessful connection.
print(responce)

# this will give just the status code of the get request. If the status code is 404 it is not found status.
print(responce.status_code)

'''
You can also make this an if statment so that if the reponce exists you can trigger true.
Under the hood the requests library had used __bool__() to replace how calling the object in an if works.
In this case if the connection status is sucessful then it will return ture and false otherwise.
'''
if responce:
    print('connection sucessful')

else:
    print('connection faled')

# lets use the wttr.in api for weather data. docs: https://github.com/chubin/wttr.in

weather = requests.get('http://wttr.in/30303')
# this will show the request data in raw bytes. This gives control, but is ugly
print(weather.content)
print()
# this will get the information in a plain text format
print(weather.text)
print()

'''
Responce headers are the meta data associated with your request.
This can give useful information aoubt he request such as when the request was made or what format the data was sent in.
Such In this case it is plain text.
'''
print(weather.headers)

'''
Json is a standard format that http requests take and give.
In python json is directly a dictionary with no changes needed.
In this case we did not request the json output so we need to chenge how we get this information.
All of this can be found in the wttr.in documentation. 
https://github.com/chubin/wttr.in
'''
jsonWeather = requests.get('http://wttr.in/30303?format=j1')
weather_dict = jsonWeather.json()
# print(weather_dict)
print()
# since this is a dictionary we can grab easy from it given a key
print(weather_dict['current_condition'][0]['temp_F'])

'''
The way this data is presented is up to the organizatoin making the api what data is sent in these requests is dicted by them. 
So the best way to use an api is to read the documentation on the api.
'''

'''
another way to acomplish the same formatiing is to use the params part of the get() function
'''

jsonWeather = requests.get(
    'http://wttr.in/30303',
    params={'format': 'j1'}
    )

print(jsonWeather)


'''
Query string parameter
This is the way you can query this particular api to get information that you are using a search function for. 
this is the 'q' parameter in the params part of the get function.
'''
weather = requests.get(
    'http://wttr.in',
    params={
        'q': 'Atlanta+Georgia',
        'format': '3'
        }
    )

print(weather.text)

'''
There are other http methods and we will cover the more in the next workshop
'''