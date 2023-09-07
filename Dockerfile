FROM python:3.8.10
RUN pip install reflex

COPY . .

RUN reflex init