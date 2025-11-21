import os
import yaml
from common import FULL_IMAGES_TRAIN, LABELS_TRAIN, FULL_IMAGES_VAL, BASE_ROOT,\
IMAGES_TRAIN, IMAGES_VAL, LABELS_VAL, DATA_YAML
def make_data_yaml(**data):
    with open(f"{data['path']}/{DATA_YAML}",'w') as f:
        yaml.safe_dump(data,f)
        
os.makedirs(FULL_IMAGES_TRAIN, exist_ok=True)
os.makedirs(LABELS_TRAIN, exist_ok=True)
os.makedirs(FULL_IMAGES_VAL, exist_ok=True)
os.makedirs(LABELS_VAL, exist_ok=True)
make_data_yaml(path=BASE_ROOT, train=IMAGES_TRAIN, val=IMAGES_VAL)
