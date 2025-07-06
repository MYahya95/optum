FROM python:3.12
ENV PYTHONUNBUFFERED=1
WORKDIR / optum
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]