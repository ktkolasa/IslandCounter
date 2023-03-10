FROM python:3.8

WORKDIR /src

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# RUN pytest