FROM python:3.8
WORKDIR /usr/src/app
RUN apt update
RUN pip3 install reflex
COPY . .
RUN reflex init
RUN reflex export --no-zip
RUN ["chmod", "+x", "./run.sh"]
EXPOSE 3000
ENTRYPOINT ["./run.sh"]