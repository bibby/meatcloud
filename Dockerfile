FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
    pkg-config \
    libpng12-dev \
    libfreetype6-dev \
    python-dev \
    python-pip \
    python-pil

RUN pip install \
    matplotlib \
    wordcloud

WORKDIR /opt/srrc
COPY meatcloud.py ./

VOLUME /opt/in
VOLUME /opt/out

CMD ["python", "meatcloud.py"]
