#!/usr/bin/python

import os
import urllib.request
import urllib.parse
import json
import dotenv

dotenv.load_dotenv()

def getAuthToken():
    url = "{}/{}/user/login".format(os.getenv("UNMS_ADDRESS"), os.getenv("UNMS_VERSION"))
    loginData = {
        'password': os.getenv("UNMS_PASSWORD"),
        'username': os.getenv("UNMS_USERNAME"),
        'sessionTimeout': 3600000
    }
    data = urllib.parse.urlencode(loginData).encode()
    req =  urllib.request.Request(url, data=data) # this will make the method "POST"
    resp = urllib.request.urlopen(req)
    responseHeaders = dict(resp.info())
    authToken = responseHeaders['x-auth-token']
    print(authToken)
    print(resp.read().decode('utf-8'))
    return authToken

def getDevices(authToken):
    url = "{}/{}/devices".format(os.getenv("UNMS_ADDRESS"), os.getenv("UNMS_VERSION"))
    req = urllib.request.Request(url)
    req.add_header('x-auth-token', authToken)
    resp = urllib.request.urlopen(req)
    data = resp.read()
    devices = json.loads(data.decode('utf-8'))
    print(devices)
    return devices

def getDeviceStats(deviceId, authToken):
    url = "{}/{}/devices/{}/statistics?interval=hour".format(os.getenv("UNMS_ADDRESS"), os.getenv("UNMS_VERSION"), deviceId)
    req = urllib.request.Request(url)
    req.add_header('x-auth-token', authToken)
    resp = urllib.request.urlopen(req)
    data = resp.read()
    stats = json.loads(data.decode('utf-8'))
    print(stats)
    return stats

def main():
    # do something here
    authToken = getAuthToken()
    devices = getDevices(authToken)
    for device in devices:
        print(device)
        if device['identification']['type'] == 'airMax' :
            getDeviceStats(device['identification']['id'], authToken)

    # while True:
    #     pass

if __name__ == '__main__':
    try:
        main()
    except (Exception,KeyboardInterrupt,SystemExit):
        quit=True
        raise
