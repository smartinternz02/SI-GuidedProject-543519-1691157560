FROM python:3.10

RUN mkdtr -p /std_app

COPY . /std_app

RUN python3 -m pip install -r /std_app/requirements.txt

EXPOSE 5000

CMD ["python","/std_app/app.py"]



