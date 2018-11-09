#Import the modules
import requests
import json

# Get the feed
#r = requests.get("https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22")
#r.text

# Convert it to a Python dictionary
#data = json.loads(r.text)
#print(data)

SERVER_URL = 'http://74.208.178.82:8080/mopAcmeService/'

END_POINT = {
    'PING' : 'component/ping',
    'LOGIN': 'login',
    'USER_DETAILS': 'component/User'
    }

requestHeaders={'Content-Type':  'application/json', 'Authorization': 'Basic null'}

saltKey = ''
accessToken = ''
def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))
    
rMopPingRequest = requests.Request('POST', '' + SERVER_URL + END_POINT['PING'], headers=requestHeaders, json={})
rMopPingRequestPrepared = rMopPingRequest.prepare()
# pretty_print_POST(rMopPingRequestPrepared)

s = requests.Session()
rMopPingResponse = s.send(rMopPingRequestPrepared)

# print(rMopPingResponse.status_code)
if (rMopPingResponse.status_code == 200):
      # print(rMopPingResponse.text)
      rMopPingResponseData = json.loads(rMopPingResponse.text)
      saltKey = rMopPingResponseData
      # print(saltKey['data'][0]['propertyValue'])
      # [0].rMopPingResponseData


if (saltKey != ''): 
    rMopLoginRequest = requests.Request('POST', '' + SERVER_URL + END_POINT['LOGIN'], headers=requestHeaders, json={"username":"pm@mopstar.us","password":"JCc72snMqmd/toZV4Y5xjIYB8uK9N6RqgCiS+/LPKjA="})
    rMopLoginRequestPrepared = rMopLoginRequest.prepare()
    rMopLoginResponse = s.send(rMopLoginRequestPrepared)
    rMopLoginResponseData = json.loads(rMopLoginResponse.text)
    
    accessToken = rMopLoginResponseData['token']
    print('accessToken', accessToken)

    if (accessToken != None or accessToken != ''):
        # get user details  
        requestHeaders['Authorization'] = 'Basic cG1AbW9wc3Rhci51czplMWQwZmQ0MmU0NWI0Nzk0NDFiZTVjMzRhMGZhYmQ2ZTBjMmQxOTAyMWI5YjA4MTIwNmUxMjNlYzY3NzA4ZDc0'
        rMopUserDetailsRequest = requests.Request('POST', '' + SERVER_URL + END_POINT['USER_DETAILS'], headers=requestHeaders, json={"FILTER":[{"FILTER_KEY":"USER_EMAIL_ID","FILTER_VALUE":"pm@mopstar.us","FILTER_TYPE":"CHARS"}]})
        rMopUserDetailsRequestPrepared = rMopUserDetailsRequest.prepare()
        rMopUserDetailsResponse = s.send(rMopUserDetailsRequestPrepared)
        rMopUserDetailsResponseData = json.loads(rMopUserDetailsResponse.text)
        print(rMopUserDetailsResponse.text)



    
