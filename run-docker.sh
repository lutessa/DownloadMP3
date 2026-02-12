#!/bin/bash

docker run -it  -u $(id -u):$(id -g) -v $(pwd)/downloads:/app --name yt-container yt-dlp:latest
