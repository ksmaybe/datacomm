FROM python:3

WORKDIR /app
COPY . .
RUN pip install Flask
RUN pip install flask_api
RUN pip install requests
RUN pip install pickle
CMD [ "python", "./AS/authoritative.py" ]
CMD [ "python", "./FS/fibonacci.py" ]
CMD [ "python", "./US/user.py" ]
CMD [ "python", "./FS/start.py" ]