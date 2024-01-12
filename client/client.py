from modules.fetch import Fetch

def main():
    apiUrl = 'http://127.0.0.1:3000'
    video1_id = 0

    print('ENVIO DE VÍDEO 1 INICIADO')
    with open('./storage/video.mp4', 'rb') as arquivo:
        blob = arquivo.read()
        video = {
            "title": 'Nuevo Video',
            "blob": blob,
            "size": len(blob)
        }
        response = Fetch.post(f'{apiUrl}/video', video)
        video1_id = response['id']
    print('ENVIO DE VÍDEO 1 FINALIZADO')

    print('ENVIO DE VÍDEO 2 INICIADO')
    with open('./storage/video2.mp4', 'rb') as arquivo:
        blob = arquivo.read()
        video = {
            "title": 'Nuevo Video 2',
            "blob": blob,
            "size": len(blob)
        }
        Fetch.post(f'{apiUrl}/video', video)
    print('ENVIO DE VÍDEO 2 FINALIZADO')

    print("BUSCA DO VÍDEO 1 INICIADA")
    video_id = video1_id
    video_obtido = Fetch.post(f'{apiUrl}/video/id', {
        "id": video_id
    })
    print(f"Vídeo obtido por ID {video_id}: {video_obtido['title']}")
    print("BUSCA DO VÍDEO 1 FINALIZADA")

    print("REMOCAO DO VÍDEO 1 INICIADA")
    video_a_remover = video1_id
    video_obtido = Fetch.delete(f'{apiUrl}/video', {
        "id": video_a_remover
    })
    if(video_obtido != None):
        print(f"Vídeo obtido por ID {video_id}: {video_obtido['title']}")
    print("REMOCAO DO VÍDEO 1 FINALIZADA")

    print("LISTAGEM DOS VÍDEOS INICIADA")
    todos_os_videos = Fetch.get(f'{apiUrl}/videos')
    print("Todos os vídeos no banco de dados:")
    for video in todos_os_videos:
        print(video['id'], video['title'])
    print("LISTAGEM DOS VÍDEOS FINALIZADA")

if __name__ == "__main__":
    main()