FROM python:3.9

RUN mkdir -p /app

COPY . main.py /app/

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

CMD [ "uvicorn main:app --reload" ]
