import sys
import os


def download(file):
    file = open(file)
    links = file.readlines()
    file.close()

    for link in links:
        os.system(
            f'youtube-dl --extract-audio --audio-format "mp3" {link}')
        print()


if __name__ == '__main__':
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print('Usage: python3 download.py links.txt')
        exit(1)

    download(sys.argv[1])
