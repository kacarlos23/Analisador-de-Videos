from pytubefix import YouTube

def main():
    url = input('URL do vídeo: ') # Pede URL do vídeo

    yt = YouTube(url)

    print(f'Título do vídeo: {yt.title}') # Exibe o título do vídeo

    stream = yt.streams.get_audio_only()

    stream.download()

if __name__ == '__main__':
    main()