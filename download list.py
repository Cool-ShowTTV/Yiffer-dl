from turtle import down
import download

with open('list.txt', 'r') as f:
    for line in f:
        comicName = line.strip()
        if comicName == '':
            continue
        download.Comic.downloadComic(comicName)