import os
import subprocess

def download_audio(video_url, output_path):
    try:
        command = [
            'yt-dlp',
            '-f', 'bestaudio',
            '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
            video_url
        ]
        subprocess.run(command, check=True)
        
        print(f"Téléchargé en audio: {video_url}")
    except Exception as e:
        print(f"Erreur lors du téléchargement de l'audio de {video_url}: {e}")

def download_playlist(playlist_url, output_path, download_type='audio'):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        print(f"Téléchargement de la playlist (ou video): {playlist_url}")
        
        if download_type == 'audio':
            command = [
                'yt-dlp',
                '--yes-playlist',
                '-f', 'bestaudio',
                '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
                playlist_url
            ]
        elif download_type == 'video':
            command = [
                'yt-dlp',
                '--yes-playlist',
                '-f', 'best[ext=mp4]',
                '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
                playlist_url
            ]
        
        subprocess.run(command, check=True)
        
        print(f"Téléchargement de la playlist (ou de la video) terminé.")
    except Exception as e:
        print(f"Erreur lors du téléchargement de la playlist: {e}")

def main():
    try:
        playlist_url = input("Entrez l'URL de la playlist YouTube: ")
        output_path = "./playlist_downloads"
        download_type = input("Souhaitez-vous télécharger en 'audio' ou 'video'? ").lower()
        
        if download_type == 'audio':
            download_playlist(playlist_url, output_path, 'audio')
        elif download_type == 'video':
            download_playlist(playlist_url, output_path, 'video')
        else:
            print("Type de téléchargement non reconnu. Veuillez choisir 'audio' ou 'video'.")

    except KeyboardInterrupt:
        print("\nTéléchargement annulé.")

if __name__ == "__main__":
    main()
