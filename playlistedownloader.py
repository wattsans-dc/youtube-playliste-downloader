import os
import subprocess
import sys

def install_choco():
    try:
        subprocess.run(["choco", "--version"], check=True)
        print("Chocolatey est déjà installé.")
    except FileNotFoundError:
        print("Installation de Chocolatey...")
        try:
            powershell_command = [
                "powershell",
                "-command",
                "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
            ]
            subprocess.run(powershell_command, check=True)
            print("Chocolatey installé avec succès.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'installation de Chocolatey : {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            sys.exit(1)

def install_ffmpeg():
    try:
        subprocess.run(["choco", "install", "-y", "ffmpeg"], check=True)
        print("FFmpeg installé avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation de FFmpeg : {e}")
        sys.exit(1)

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

def download_playlist(playlist_url, output_path, download_type='audio'):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        print(f"Téléchargement de la playlist (ou video): {playlist_url}")
        
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
        
        print(f"Téléchargement de la playlist (ou de la video) terminé.")
    except Exception as e:
        print(f"Erreur lors du téléchargement de la playlist: {e}")

def main():
    try:
        install_choco()
        install_ffmpeg()
        
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
