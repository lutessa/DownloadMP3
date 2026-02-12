FROM ubuntu:22.04

ARG USER_ID
ARG GROUP_ID
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user


WORKDIR /app

COPY . .

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y   
RUN pip install yt-dlp

