#!/usr/bin/python

import os
import dotenv
import unms

dotenv.load_dotenv()

def main():
    # do something here
    unmsClient = unms.Client(os.getenv("UNMS_ADDRESS"), os.getenv("UNMS_VERSION"))
    unmsClient.authenticate(os.getenv("UNMS_USERNAME"), os.getenv("UNMS_PASSWORD"))
    devices = unmsClient.getDevices()
    for device in devices:
        if device['identification']['type'] == 'airMax' :
            unmsClient.getDeviceStats(device['identification']['id'])

    # while True:
    #     pass

if __name__ == '__main__':
    try:
        main()
    except (Exception,KeyboardInterrupt,SystemExit):
        quit=True
        raise
