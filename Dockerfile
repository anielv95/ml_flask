FROM python:3.11.3
WORKDIR /gh
COPY ./requirements.txt ./
COPY ./predict.py ./
RUN pip install  --no-cache-dir -r requirements.txt &&\
    gunicorn --bind 0.0.0.0:8585 predict:app
CMD ["python","predict-test.py"]