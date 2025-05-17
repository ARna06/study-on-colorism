import os
import pandas as pd
import numpy as np

base_dir = "data/"  

roles = ["actor", "actress", "side_actor", "side_actress"]

all_data = []

for year_folder in sorted(os.listdir(base_dir)):
    year_path = os.path.join(base_dir, year_folder)
    if os.path.isdir(year_path) and year_folder.startswith("year_"):
        year = int(year_folder.split("_")[1])
        for movie_folder in os.listdir(year_path):
            movie_path = os.path.join(year_path, movie_folder)
            if os.path.isdir(movie_path):
                for role in roles:
                    file_path = os.path.join(movie_path, f"{role}.csv")
                    if os.path.exists(file_path):
                        array = np.loadtxt(file_path, delimiter=',', skiprows=1)
                        skin_tone = np.mean(array)
                        data = {
                            'role': role, 
                            'movie': movie_folder,
                            'year': year,
                            'L': skin_tone
                        }
                        df = pd.DataFrame(data, index=[0])
                        all_data.append(df)

data = pd.concat(all_data, ignore_index=True)
#print(data.head())

data['role_type'] = data['role'].apply(lambda x: 'lead' if 'side' not in x else 'side')
data['gender'] = data['role'].apply(lambda x: 'male' if 'actor' in x else 'female')