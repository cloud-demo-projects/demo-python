FROM python:3.10

WORKDIR /exchange

COPY requirements.txt .

RUN pip install -r requirements_prod.txt

COPY src/ .

CMD [ "python", "./diagram_solutions.py" ]
