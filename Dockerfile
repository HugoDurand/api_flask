FROM python:3.6.7
ADD . /code
WORKDIR /code
EXPOSE 5000
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python api.py
