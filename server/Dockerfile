FROM python:2.7
ADD . /code
WORKDIR /code

RUN apt-get install libjpeg-dev
RUN pip install -r requirements.txt
CMD ["python", "rest.py"]
