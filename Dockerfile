FROM python:3.6
COPY . /app
WORKDIR /app
RUN set -xe \
    && apt-get update -y \
    && apt-get install python3-pip -y \
    && apt-get install libssl-dev libffi-dev -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
LABEL maintainer=abdellatif
EXPOSE 5000 
CMD ["python","app.py"]
