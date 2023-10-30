FROM python:3.8
WORKDIR /usr/src/app
RUN pip3 install reflex
COPY . .
RUN ["chmod", "+x", "./run.sh"]
EXPOSE 3000 8000
ENTRYPOINT ["./run.sh"]