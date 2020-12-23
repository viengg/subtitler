import os
import glob
import sys

path = input("Caminho do diretório com os arquivos> ").replace('\\', "/")
os.chdir(path)
ext_video = input("Tipo de arquivo de video> ")
ext_subtitle = "srt"
#ext_subtitle = input("Tipo de arquivo de legenda> ")
videos = glob.glob("*." + ext_video)
subtitles = glob.glob("*." + ext_subtitle)

for video, subtitle in zip(videos, subtitles):
    file_name = video[:-4]
    os.rename(subtitle, file_name + "." + ext_subtitle)

