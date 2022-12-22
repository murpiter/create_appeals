FROM python:3.10.8

WORKDIR /usr/app/backend/src

COPY backend/src ./
ADD backend/requirements.txt /usr/app/backend/src
RUN pip install -r ./requirements.txt

CMD [ "python", "src/server.py"]