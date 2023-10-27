FROM python:3.8
WORKDIR /usr/src/app
RUN pip3 install reflex
COPY . .
RUN ["chmod", "+x", "./run.sh"]
ENTRYPOINT ./run.sh