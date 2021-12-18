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
COPY startup.sh /startup.sh
RUN chmod 744 /startup.sh
CMD ["/startup.sh"]
# CMD ["python", "manage.py", "migrate"]
# ENTRYPOINT ["python", "manage.py", "migrate"]
# ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]