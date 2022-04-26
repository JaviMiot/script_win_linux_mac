FROM python:3
WORKDIR /usr/code
COPY ["./requirements", "/requirements"]
RUN pip install -r /requirements/production.txt
COPY ["./src", "/usr/code"]
CMD ["python","./src/main.py" ]