FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app/backend
COPY . /app/backend

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
