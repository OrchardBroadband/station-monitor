#!/usr/bin/python

import os
import dotenv
import unms
from influxdb import InfluxDBClient

dotenv.load_dotenv()

def translate(device, stats):
    influxData = []
    deviceName = device['identification']['name']
    deviceModel = device['identification']['model']
    deviceMAC = device['identification']['mac']
    for interface in stats['interfaces']:
        interfaceName = interface['name']
        for receiveData in interface['receive']:
            timestamp = receiveData['x']
            value = receiveData['y']
            influxData.append({
                "measurement": "throughput",
                "tags": {
                    "int": interfaceName,
                    "name": deviceName,
                    "mac": deviceMAC,
                    "dir": "rx"
                },
                "time": timestamp * 1000000, # must be in nanoseconds
                "fields": {
                    "value": value
                }
            })
        for receiveData in interface['transmit']:
            timestamp = receiveData['x']
            value = receiveData['y']
            influxData.append({
                "measurement": "throughput",
                "tags": {
                    "int": interfaceName,
                    "name": deviceName,
                    "mac": deviceMAC,
                    "dir": "tx"
                },
                "time": timestamp * 1000000, # must be in nanoseconds
                "fields": {
                    "value": value
                }
            })
    return influxData

def main():
    # do something here
    unmsClient = unms.Client(os.getenv("UNMS_ADDRESS"), os.getenv("UNMS_VERSION"))
    unmsClient.authenticate(os.getenv("UNMS_USERNAME"), os.getenv("UNMS_PASSWORD"))
    devices = unmsClient.getDevices()
    influxData = []
    for device in devices:
        if device['identification']['type'] == 'airMax' :
            stats = unmsClient.getDeviceStats(device['identification']['id'])
            influxData += translate(device, stats)

    influxDBClient = InfluxDBClient(os.getenv("INFLUXDB_ADDRESS"), os.getenv("INFLUXDB_PORT"), os.getenv("INFLUXDB_USERNAME"), os.getenv("INFLUXDB_PASSWORD"), os.getenv("INFLUXDB_DATABASE"))
    influxDBClient.write_points(influxData)

    # while True:
    #     pass

if __name__ == '__main__':
    try:
        main()
    except (Exception,KeyboardInterrupt,SystemExit):
        quit=True
        raise
