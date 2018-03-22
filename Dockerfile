FROM python:3

ADD service.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./service.py" ]
