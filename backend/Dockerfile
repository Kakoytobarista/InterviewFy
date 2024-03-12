FROM python:3.11.2

WORKDIR /backend

COPY ./src /backend/src
COPY ./.env /backend/
COPY ./main.py /backend/
COPY ./__init__.py /backend/
COPY ./requirements.txt /backend/

RUN pip install -r /backend/requirements.txt

ENV PYTHONPATH=/backend

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
