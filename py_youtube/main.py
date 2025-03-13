import pandas as pd
import pytube
import logging
from concurrent.futures import ThreadPoolExecutor

# Setup logging
logging.basicConfig(level=logging.INFO)

def download_video(name, link):
    try:
        yt = pytube.YouTube(link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(filename=name)
        logging.info(f"Downloaded: {name}")
    except Exception as e:
        logging.error(f"Error downloading {link}: {e}")

def download_videos(videos_data):
    with ThreadPoolExecutor(max_workers=min(videos_data.size, 10)) as executor:
        for name, link in videos_data.itertuples(index=False):
            print('Downloading', link, 'as', name)
            executor.submit(download_video, name, link)

if __name__ == "__main__":
    file_path = input("Enter the path to your Excel file: ")
    try:
        df = pd.read_excel(file_path)
        if df.columns[0] != 'name' or df.columns[1] != 'uurl':
            raise ValueError("Could not parse spreadsheet")
        download_videos(df)
    except Exception as e:
        logging.error(f"Failed to process the Excel file: {e}")
