from cv2.typing import MatLike
from typing import List, Any
from numpy.typing import NDArray
from skimage import color
import numpy as np

def extract_glabella_color(face_locations:NDArray[np.float64] | Any | None, frame: MatLike) -> List[float]:
    luminance = list()
    if not face_locations:
        raise ValueError("No face locations provided")
    for face in face_locations:
        keypoints = face['keypoints']
        left_eyebrow = keypoints['left_eye']
        right_eyebrow = keypoints['right_eye']
        glabella_x = (left_eyebrow[0] + right_eyebrow[0]) // 2
        glabella_y = (left_eyebrow[1] + right_eyebrow[1]) // 2
        
        glabella_patch = frame[glabella_y-2:glabella_y+2, glabella_x-2:glabella_x+2]
        patch_lab = color.rgb2lab(glabella_patch / 255.0)
        
        l_values = patch_lab[:, :, 0] 
        luminance.append( np.mean(l_values))
    return luminance 
