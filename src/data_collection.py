import yt_dlp
import os

def download_movies(url, save_path):
    ydl_opts = {
        'format': 'best[ext=mp4][height<=720]',
        'outtmpl': save_path,
        'quiet': False,
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

trailer_urls_and_names = {
    "2024" : {
        "name": "url",
    },
    "2023" : {
        "name": "url",
    },
    "2022" : {
        "name": "url",
    },
    "2021" : {
        "name": "url",
    },
    "2020" : {
        "name": "url",
    },
    "2019" : {
        "name": "url",
    },
    "2018" : {
        "name": "url",
    },
    "2017" : {
        "name": "url",
    },
    "2016" : {
        "name": "url",
    },
    "2015" : {
        "name": "url",
    },
}

if __name__ == "__main__":
    for year, movies in trailer_urls_and_names.items():
        for movie, url in movies.items():
            try:
                video_path = f"movies/year_{year}/{movie}/{movie}.mp4"
                download_movies(url, video_path)
                print(f"Downloaded {movie} for {year}")
            except Exception as e:
                print(f"Failed to download {movie}: {e}")