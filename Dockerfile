FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY manage.py/ app/manage.py
COPY tests /app/tests
COPY templates /app/templates
COPY static /app/static
COPY tests /app/tests

