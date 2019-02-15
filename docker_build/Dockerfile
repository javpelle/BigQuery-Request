FROM python:3

RUN pip install pandas

RUN pip install google-cloud-bigquery

VOLUME /data

ADD ./Query.py /

CMD [ "python", "./Query.py" ]
