FROM python:3.7-alpine

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5002

CMD ["python", "meraki_sample_location_scanning_receiver.py", "-v", "simulator", "-s", "simulator"]