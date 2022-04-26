FROM python:3
WORKDIR /usr/code
COPY ["./requirements", "/requirements"]
RUN pip install -r /requirements/local.txt
CMD ["python","./src/main.py" ]