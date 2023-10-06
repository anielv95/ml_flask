install:
		pip install --upgrade pip &&\
				pip install -r requirements.txt
			
make endpoint:
		gunicorn --bind 0.0.0.0:8585 predict:app