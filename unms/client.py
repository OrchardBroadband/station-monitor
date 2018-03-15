import json
import urllib.request
import urllib.parse


class Client:
    def __init__(self, unmsAddress, unmsVersion):
        self.origin = "{}/{}".format(unmsAddress, unmsVersion)

    def authenticate(self, username, password):
        url = "{}/user/login".format(self.origin)
        loginData = {
            'password': password,
            'username': username,
            'sessionTimeout': 3600000
        }
        data = urllib.parse.urlencode(loginData).encode()
        req = urllib.request.Request(url, data=data) # this will make the method "POST"
        resp = urllib.request.urlopen(req)
        responseHeaders = dict(resp.info())
        self.authToken = responseHeaders['x-auth-token']

    def getAuthToken(self):
        return self.authToken

    def getDevices(self):
        url = "{}/devices".format(self.origin)
        req = urllib.request.Request(url)
        req.add_header('x-auth-token', self.getAuthToken())
        resp = urllib.request.urlopen(req)
        data = resp.read()
        devices = json.loads(data.decode('utf-8'))
        return devices

    def getDeviceStats(self, deviceId):
        url = "{}/devices/{}/statistics?interval=hour".format(self.origin, deviceId)
        req = urllib.request.Request(url)
        req.add_header('x-auth-token', self.getAuthToken())
        resp = urllib.request.urlopen(req)
        data = resp.read()
        stats = json.loads(data.decode('utf-8'))
        return stats
