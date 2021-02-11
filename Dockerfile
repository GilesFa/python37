FROM python:3.8

RUN mkdir /python

COPY guessnumber.py /python

CMD ["python","/python/guessnumber.py"]