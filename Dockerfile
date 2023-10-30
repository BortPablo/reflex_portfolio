FROM python:3.8
WORKDIR /usr/src/app
RUN pip3 install reflex
COPY . .
RUN reflex init --loglevel debug
RUN ["chmod", "+x", "/root/.bashrc"]
RUN /bin/sh -c /root/.bashrc
RUN reflex export --no-zip --loglevel debug
RUN ["chmod", "+x", "./run.sh"]
EXPOSE 3000 8000
ENTRYPOINT ["./run.sh"]