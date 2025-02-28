FROM python:3.9-slim

# Sabse pehle pip, setuptools aur wheel ko upgrade karein
RUN pip install --upgrade pip setuptools wheel

# Ab aapki repository ke files copy karein
WORKDIR /app
COPY . /app

# Requirements install karein
RUN pip install -r requirements.txt

# Container start hone par start.sh run ho
CMD ["bash", "start.sh"]
