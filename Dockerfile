FROM python
RUN pip install reflex

COPY . .

RUN reflex init