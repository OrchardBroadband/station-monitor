# station-monitor
Scripts to augment station (CPE) monitoring provided by UNMS

First Time
1. Create `.env` with these keys set:
  - `INFLUXDB_ADDRESS`
  - `INFLUXDB_PORT`
  - `INFLUXDB_USERNAME`
  - `INFLUXDB_PASSWORD`
  - `INFLUXDB_DATABASE`
  - `UNMS_ADDRESS`
  - `UNMS_VERSION`
  - `UNMS_USERNAME`
  - `UNMS_PASSWORD`
2. Create virtual environment `python -m venv ./venv`

Each Time
1. Activate virtual environment
  - Linux `source ./venv/bin/activate`
  - Windows `venv\Scripts\activate.bat` - not in PowerShell
2. Install packages `pip install -r requirements.txt`
3. Hack away

When Done
1. Deactivate virtual environment `deactivate`

Running
1. `nohup python3 service.py &`
or
1. `docker-compose up -d`
