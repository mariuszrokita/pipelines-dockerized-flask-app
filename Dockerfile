# TODO: Try to use lighter base docker image.
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

# Install required packages
COPY requirements.txt /app/
RUN pip3 install -r   /app/requirements.txt

COPY app.py     /app/
COPY config.cfg /app/

WORKDIR /app

# Run Flask app
CMD ["python3", "app.py"]

# Explicitly inform what ports are in use
EXPOSE 5000