FROM  python:3.8-slim-buster

EXPOSE 5000

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

CMD [ "python","search.py" ]