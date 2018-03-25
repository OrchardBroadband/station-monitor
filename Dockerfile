FROM python:3

WORKDIR /usr/local/bin

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "./service.py" ]
