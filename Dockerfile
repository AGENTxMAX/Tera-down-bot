FROM python:3.10-slim

# APT packages update karein aur unnecessary dependencies na install karein
RUN apt-get update && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Pip, setuptools aur wheel ko upgrade karein
RUN pip install --upgrade pip setuptools wheel

WORKDIR /app

# Repository ke sabhi files copy karein
COPY . /app

# Python dependencies install karein
RUN pip install -r requirements.txt

# Container start hone par start.sh script run karein
CMD ["bash", "start.sh"]