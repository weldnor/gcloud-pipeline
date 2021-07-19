FROM python:3-alpine3.14

COPY * ./

RUN pip3 install -r requirements.txt

ENV PORT 8080
EXPOSE $PORT

ENTRYPOINT ["python3", "main.py"]