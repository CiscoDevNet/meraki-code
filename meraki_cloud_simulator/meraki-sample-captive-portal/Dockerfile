FROM python:3.7-alpine

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5004

CMD ["python", "meraki_sample_captive_portal.py", "-n", "Simulated Network", "-s", "Simulated SSID", "-p", "simulatedpassword"]