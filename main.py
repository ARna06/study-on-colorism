from src.face_tracer import FaceDetector
from src.pixel_sampler import extract_glabella_color
import numpy as np

file_path = "file/to/movie.mp4"
movie = FaceDetector(file_path)

movie.detect_faces(20)
movie.draw_faces()
pixel_vals_lead1 = extract_glabella_color(movie.faces, movie.frame)

movie.detect_faces(18)
movie.draw_faces()
pixel_vals_lead2 = extract_glabella_color(movie.faces, movie.frame)

movie.detect_faces(98)
movie.draw_faces()
pixel_vals_side_male = np.array(extract_glabella_color(movie.faces, movie.frame)).mean()

movie.detect_faces(57)
movie.draw_faces()
pixel_vals_side_fem = np.array(extract_glabella_color(movie.faces, movie.frame)).mean()