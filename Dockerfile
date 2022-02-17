FROM python:3

ENV PYTHONBUFFERED 1

# Upgrade Pip
RUN pip install --upgrade pip

# Create a folder, Copy content and Install dependencies
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

# To access from outside the container
EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]