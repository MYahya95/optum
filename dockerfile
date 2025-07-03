FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir / optum
WORKDIR / optum
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]