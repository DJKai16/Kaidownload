from pytube import YouTube
import os

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"\033[36mProgreso: {percentage:.1f}%\033[0m", end="\r")

def select_resolution(video):
    available_resolutions = video.streams.filter(file_extension='mp4').order_by('resolution').desc()
    print("\033[33mResoluciones disponibles para el video:")
    for i, stream in enumerate(available_resolutions, start=1):
        print(f"{i}. {stream.resolution} ({stream.mime_type.split('/')[1].upper()})")
    option = int(input("\033[37mSelecciona el número de la resolución que deseas descargar: "))
    return available_resolutions[option - 1]

def select_audio_quality(video):
    available_audio = video.streams.filter(only_audio=True).order_by('abr').desc()
    print("\033[33mCalidades disponibles para el audio:")
    for i, stream in enumerate(available_audio, start=1):
        print(f"{i}. {stream.abr} kbps")
    option = int(input("\033[37mSelecciona el número de la calidad que deseas descargar: "))
    return available_audio[option - 1]

def reload_video(video_url):
    try:
        video = YouTube(video_url, on_progress_callback=on_progress)
        print(f"\033[35mVideo encontrado: {video.title}")

        print("\033[33mOpciones de descarga:")
        print("1. Video (MP4)")
        print("2. Solo Audio (MP3)")

        option = input("\033[37mSelecciona el número de la opción que deseas descargar: ")

        if option == "1":
            stream = select_resolution(video)
            print(f"\033[33mDescargando video (MP4) en {stream.resolution}: {video.title}")
            file_name = "danjah_" + video.title + ".mp4"
            destination = os.path.join(os.getcwd(), file_name)
            stream.download(output_path=os.getcwd(), filename=file_name)
            print("\033[32mDescarga de video (MP4) completada con éxito.")
        elif option == "2":
            stream = select_audio_quality(video)
            print(f"\033[33mDescargando audio (MP3) en {stream.abr} kbps: {video.title}")
            file_name = "danjah_" + video.title + ".mp3"
            destination = os.path.join(os.getcwd(), file_name)
            stream.download(output_path=os.getcwd(), filename=file_name)
            print("\033[32mDescarga de audio (MP3) completada con éxito.")
        else:
            print("\033[31mOpción no válida. Asegúrate de seleccionar la opción correcta.")

    except Exception as e:
        print(f"\033[31mError durante la recarga: {e}")

if __name__ == "__main__":
    print("\033[35mBienvenido a DANJAH videos.")
    video_url = input("\033[33mIngresa la URL del video que desea descargar: ")

    reload_video(video_url)
