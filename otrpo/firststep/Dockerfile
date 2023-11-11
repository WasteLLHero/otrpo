FROM python:3.11.2

ENV PYTHONDONTWRITEVYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /otrpo-1/otrpo/firststep

COPY requirements.txt /otrpo-1/otrpo/firststep

RUN pip install -r requirements.txt

COPY . /otrpo-1/otrpo/firststep

# EXPOSE 8000
# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
