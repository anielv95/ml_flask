FROM python:3.11.3
WORKDIR /gh
COPY ./requirements.txt ./predict.py ./predict-test.py ./
RUN pip install  --no-cache-dir -r requirements.txt
EXPOSE 8585
ENTRYPOINT ["gunicorn","--bind","0.0.0.0:8585","predict:app"]