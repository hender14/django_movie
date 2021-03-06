FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
# WORKDIR /code
# COPY requirements.txt /code/
COPY requirements.txt .
RUN pip install -r requirements.txt && apt update && apt-get install -y libgl1-mesa-dev
# COPY . /code/
COPY . .
# COPY manage.py .