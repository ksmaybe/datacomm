FROM python:3

WORKDIR /app
COPY . .
RUN pip install Flask
CMD [ "python", "./time-app.py" ]