FROM python:3.13-slim

RUN apt-get update -y && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone https://github.com/MrEchoFi/GreeDoS_V2.git

WORKDIR /app/GreeDoS_V2

RUN pip install -r requirements.txt

#Run Scripts When Container Starts

CMD ["python3", "GreeDoS_ii.py"]
