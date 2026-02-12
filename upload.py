import os
import requests
import shutil

VLC_URL = "http://192.168.15.12/upload.json" 
FOLDER_PATH = "./downloads"
UPLOADED_FOLDER = "./uploaded"

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "http://192.168.15.12/",
    "Origin": "http://192.168.15.12/"
}

def upload_file(filepath):
    filename = os.path.basename(filepath)

    with open(filepath, "rb") as f:
        files = {
            "files[]": (filename, f, "audio/mpeg")
        }

        print(f"Uploading {filename}...")
        response = requests.post(
            VLC_URL,
            headers=headers,
            files=files
        )

    if response.status_code == 200:
        print(f"✅ Success: {filename}")
        return True
    else:
        print(f"❌ Failed: {filename} | {response.status_code}")
        print(response.text)
        return False

def upload_album(album_path):
    album_name = os.path.basename(album_path)
    print(f"Uploading album: {album_name}")

    files_to_upload = []
    open_files = []
    success =  True
    for file in os.listdir(album_path):
        if file.lower().endswith(".mp3"):
            full_path = os.path.join(album_path, file)

            with open(full_path, "rb") as f:
                filename = os.path.basename(full_path)
                files = {
                    "files[]": (os.path.join(album_name,filename    ), f, "audio/mpeg")
                }
                data = {
                    "directory": f"/{album_name}"
                }
                print(f"Uploading {filename}...")
                response = requests.post(
                    VLC_URL,
                    headers=headers,
                    files=files
                )

            if response.status_code == 200:
                print(f"✅ Success: {filename}")
            else:
                print(f"❌ Failed: {filename} | {response.status_code}")
                print(response.text)
                success = False
                
    return success


def move(album_path):
    album_name = os.path.basename(album_path)
    destination = os.path.join(UPLOADED_FOLDER, album_name)

    shutil.move(album_path, destination)
def upload_all(folder):
    for album in os.listdir(folder):
        album_path = os.path.join(folder, album)
        if os.path.isdir(album_path):
            success = upload_album(album_path)
            if success:
                move(album_path)
        elif album_path.endswith(".mp3"):
            success = upload_file(album_path)
            if success:
                move(album_path)
    


if __name__ == "__main__":
    upload_all(FOLDER_PATH)
