import requests 
import cv2
import numpy as np
from sklearn.cluster import KMeans

def getImage(url):
    f = requests.get(url, allow_redirects=True)
    open('cover.png', 'wb').write(f.content)


def is_grayscale(image):
    # Prüfen, ob das Bild schwarz-weiß ist (kleine Abweichung in RGB-Kanälen)
    if len(image.shape) < 3 or image.shape[2] != 3:
        return True
    diff = np.abs(image[:, :, 0] - image[:, :, 1]) + np.abs(image[:, :, 1] - image[:, :, 2])
    return np.mean(diff) < 10  # Toleranzschwelle für Unterschiede

def filter_black_white(colors, threshold_black=80, threshold_white=215):
    filtered_colors = []
    for color in colors:
        brightness = np.mean(color)
        if brightness > threshold_black and brightness < threshold_white:
            filtered_colors.append(color)
            if(len(filtered_colors) >= 3): return filtered_colors
    return filtered_colors

def filter_saturation(colors, min_saturation=60, min_brightness=50):
    filtered_colors = []
    # Farben in den HSV-Farbraum konvertieren
    hsv_colors = cv2.cvtColor(np.uint8(colors.reshape(1, -1, 3)), cv2.COLOR_RGB2HSV).reshape(-1, 3)
    for i, color in enumerate(hsv_colors):
        saturation = color[1]
        brightness = color[2]
        # Sättigungs- und Helligkeitsbedingungen
        if saturation >= min_saturation and brightness >= min_brightness:
            filtered_colors.append(colors[i])
    return filtered_colors

def extract_dominant_colors(url, k=5, min_saturation=60, min_brightness=50):
    getImage(url)
    # Bild laden
    image = cv2.imread('./cover.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Bildgröße anpassen
    resized_image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_AREA)
    reshaped_image = resized_image.reshape(-1, 3)
    
    # K-Means-Clustering
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(reshaped_image)
    
    # Clusterzentren sortieren nach Sättigung und Helligkeit
    centers = kmeans.cluster_centers_
    
    if is_grayscale(image):
        # Wenn das Bild schwarz-weiß ist, keine Farben filtern
        return centers
    else:
        # Schwarz und Weiß filtern
        centers = filter_saturation(centers, min_saturation=min_saturation, min_brightness=min_brightness)
        return centers