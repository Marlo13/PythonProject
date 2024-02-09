FROM python:3.8-slim-buster

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code



CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]



# commande a faire pour lancer le docker :
# docker run  -p 3000:3000 testcci
