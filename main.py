import youtube_dl


def youtube_download(listaMusicas):
  ytdl_options = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(title)s.mp3',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
  }

  ytdl = youtube_dl.YoutubeDL(ytdl_options)
  i = 0
  for x in listaMusicas:
    nome_musica = listaMusicas[i]
    video = ytdl.extract_info(f"ytsearch:{nome_musica}", download=True)['entries'][0]
    print(f'Musica ({i+1}) - {nome_musica} - Baixada')
    i = i + 1
    

def ler_arquivo():
  abrirArquivo = open("musicas.txt", "r")
  lerLinhas = abrirArquivo.readlines()
  i = 0
  for x in lerLinhas:
    lerLinhas[i] = lerLinhas[i].replace("\n","")
    i = i + 1
  return lerLinhas


def main():
  print('Inicializando Programa!')
  listaMusicas = ler_arquivo()
  youtube_download(listaMusicas)

main()