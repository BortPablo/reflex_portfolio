FROM python:3.8
WORKDIR /usr/src/app
# RUN apt update
# RUN apt install nodejs -y
# RUN apt install npm -y
RUN pip3 install reflex
COPY . .
RUN ["chmod", "+x", "./run.sh"]
ENTRYPOINT ./run.sh