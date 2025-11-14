from ultralytics import YOLO
class ImageInfo :
    def __init__(self, pathImage):
        model = YOLO('yolov8m-seg.pt')
        boxes = model('street.jpg')[0].boxes