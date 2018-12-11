FROM python:2.7
ADD . /code
WORKDIR /code

RUN apt-get install libjpeg-dev
RUN pip install -r requirements.txt

RUN echo "Running data generator... This could take a while"
RUN "python contentGenerator.py"

CMD ["python", "rest.py"]
