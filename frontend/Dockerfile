FROM python:3.9.12

RUN pip install --upgrade pip
RUN pip install streamlit google.auth

EXPOSE 8080

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

WORKDIR /app
COPY main.py .
CMD streamlit run main.py \
    --browser.serverAddress="0.0.0.0" \
    --server.port="8080"