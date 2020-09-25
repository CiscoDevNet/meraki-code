FROM python:3.7-alpine

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5001

ENTRYPOINT ["python", "meraki_cloud_simulator.py"]