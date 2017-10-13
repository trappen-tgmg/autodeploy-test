FROM python:3-alpine

RUN pip install flask gunicorn
COPY . /app
WORKDIR /app
CMD ["gunicorn", "timr:app", "-b", "0.0.0.0:80"]
