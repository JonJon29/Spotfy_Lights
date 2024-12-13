import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def extract_dominant_colors(image_path, k=5):
    # Bild laden
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Bildgröße anpassen (schnelleres Clustering)
    resized_image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_AREA)
    reshaped_image = resized_image.reshape(-1, 3)
    
    # K-Means-Clustering
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(reshaped_image)
    
    # Clusterzentren sortieren nach Sättigung und Helligkeit
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    # Sättigung und Helligkeit berechnen
    hsv_centers = cv2.cvtColor(np.uint8(centers.reshape(1, -1, 3)), cv2.COLOR_RGB2HSV).reshape(-1, 3)
    sorted_indices = np.argsort(-hsv_centers[:, 1])  # Sortierung nach Sättigung (absteigend)
    sorted_centers = centers[sorted_indices]
    
    return sorted_centers
