FROM python:3.8.2
COPY . /app
WORKDIR /app
#RUN python3 -m pip install -r requirements.txt
EXPOSE 5010
CMD ["python3","manage.py"]
