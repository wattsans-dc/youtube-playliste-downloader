import os
import subprocess
from pydub import AudioSegment

def download_and_convert(video_url, output_path):
    try:
        command = [
            'yt-dlp',
            '-x', '--audio-format', 'mp3',
            '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
            video_url
        ]
        subprocess.run(command, check=True)
        
        print(f"Téléchargé et converti: {video_url}")
    except Exception as e:
        print(f"Erreur lors du téléchargement ou de la conversion de {video_url}: {e}")

def download_playlist(playlist_url, output_path):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        print(f"Téléchargement de la playlist: {playlist_url}")
        
        command = [
            'yt-dlp',
            '--yes-playlist',
            '-x', '--audio-format', 'mp3',
            '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
            playlist_url
        ]
        subprocess.run(command, check=True)
        
        print(f"Téléchargement de la playlist terminé.")
    except Exception as e:
        print(f"Erreur lors du téléchargement de la playlist: {e}")

playlist_url = input("Entrez l'URL de la playlist YouTube: ")

output_path = "./playlist_mp3"

download_playlist(playlist_url, output_path)
