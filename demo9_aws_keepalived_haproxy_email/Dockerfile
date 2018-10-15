FROM python:2.7
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt
ADD . /code
expose 80
CMD python app.py
