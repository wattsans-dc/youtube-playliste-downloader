import os
import subprocess

def download_audio(video_url, output_path):
    try:
        command = [
            'yt-dlp',
            '-x', '--audio-format', 'mp3',
            '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
            video_url
        ]
        subprocess.run(command, check=True)
        
        print(f"Téléchargé et converti en audio: {video_url}")
    except Exception as e:
        print(f"Erreur lors du téléchargement ou de la conversion en audio de {video_url}: {e}")

def get_best_video_format(video_url):
    try:
        command = [
            'yt-dlp',
            '--get-best',
            '--no-playlist',
            '--format', 'best',
            '--skip-download',
            '--print-json',
            video_url
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Erreur lors de la récupération du meilleur format vidéo pour {video_url}: {e}")
        return None

def download_video(video_url, output_path):
    try:
        best_format_info = get_best_video_format(video_url)
        if best_format_info:
            best_format = best_format_info.split('\n')[-1]
            command = [
                'yt-dlp',
                '-f', best_format.split()[0],
                '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
                video_url
            ]
            subprocess.run(command, check=True)
            print(f"Téléchargé en vidéo: {video_url}")
    except Exception as e:
        print(f"Erreur lors du téléchargement de la vidéo {video_url}: {e}")

def download_playlist(playlist_url, output_path, download_type='audio'):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        print(f"Téléchargement de la playlist: {playlist_url}")
        
        if download_type == 'audio':
            command = [
                'yt-dlp',
                '--yes-playlist',
                '-x', '--audio-format', 'mp3',
                '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
                playlist_url
            ]
        elif download_type == 'video':
            command = [
                'yt-dlp',
                '--yes-playlist',
                '--format', 'bestvideo+bestaudio/best',
                '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
                playlist_url
            ]
        
        subprocess.run(command, check=True)
        
        print(f"Téléchargement de la playlist terminé.")
    except Exception as e:
        print(f"Erreur lors du téléchargement de la playlist: {e}")

def main():
    try:
        playlist_url = input("Entrez l'URL de la playlist YouTube: ")
        output_path = "./playlist_downloads"
        download_type = input("Souhaitez-vous télécharger en 'audio' ou 'video'? ").lower()
        
        if download_type == 'audio':
            download_audio(playlist_url, output_path)
        elif download_type == 'video':
            download_playlist(playlist_url, output_path, 'video')
        else:
            print("Type de téléchargement non reconnu. Veuillez choisir 'audio' ou 'video'.")

    except KeyboardInterrupt:
        print("\nTéléchargement annulé.")

if __name__ == "__main__":
    main()
