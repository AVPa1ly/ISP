FROM python:3
WORKDIR /usr/src/test
ADD ./requirements.txt /usr/src/test/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && rm /usr/src/test/requirements.txt
ADD main.py .
CMD ["python", "main.py"]
