FROM ubuntu:22.04
RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/00-docker
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker
RUN DEBIAN_FRONTEND=noninteractive \
  apt-get update \
  && apt-get install -y python3 python3-pip\
  && rm -rf /var/lib/apt/lists/*
COPY . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]
