FROM ubuntu:latest

LABEL version="0.1.0"

WORKDIR /srv

RUN apt update && \
    apt install -y python3-pip libssl-dev
# install package locally (for development)
COPY . .
RUN python3 -m pip install .

# run wellness bot
CMD [ "start" ]