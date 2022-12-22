FROM python:3.10.8

WORKDIR /usr/app/servicedb/src

COPY servicedb/src ./
ADD servicedb/requirements.txt /usr/app/servicedb/src
ADD servicedb/run.py ./

RUN pip install -r ./requirements.txt
#CMD [ "ls", "-l"]
#CMD [ "ls", "-l", "src"]

CMD [ "python", "run.py"]