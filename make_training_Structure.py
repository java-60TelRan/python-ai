import os
BASE_ROOT = "datasets/"
BASE_IMAGES = BASE_ROOT + "images/"
BASE_LABELS = BASE_ROOT + "labels/"
IMAGES_TRAIN = BASE_IMAGES + "train"
LABELS_TRAIN = BASE_LABELS + "train"
IMAGES_VAL = BASE_IMAGES + "val"
LABELS_VAL = BASE_LABELS + "val"
os.makedirs(IMAGES_TRAIN, exist_ok=True)
os.makedirs(LABELS_TRAIN, exist_ok=True)
os.makedirs(IMAGES_VAL, exist_ok=True)
os.makedirs(LABELS_VAL, exist_ok=True)