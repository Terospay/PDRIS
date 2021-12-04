FROM python:3.9-alpine
COPY requirements.txt .
COPY find_links.py .
RUN pip install -r requirements.txt
CMD [ "python", "./find_links.py"]