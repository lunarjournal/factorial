# syntax=docker/dockerfile:1
FROM python:3
ADD solution.py /
RUN pip3 install numpy
ENTRYPOINT ["python3","./solution.py"]