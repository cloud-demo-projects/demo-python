FROM python:3.10

WORKDIR /exchange

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./diagrams/diagram_solution.py" ]
