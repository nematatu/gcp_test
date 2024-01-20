FROM python:3.9.12

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn

EXPOSE 8080

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

WORKDIR /app
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port","8080"]