#!/bin/bash

yt-dlp -t mp3 --embed-thumbnail -o "./%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s" --embed-metadata $1
