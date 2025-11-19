from ultralytics import YOLO
from common import BASE_ROOT
model = YOLO("yolov8m.pt")
model.train(data=BASE_ROOT + "/data.yaml", epochs=50, imgsz=256, batch=2, name="circle_square_exp")