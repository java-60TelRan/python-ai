from ultralytics import YOLO
from pandas import DataFrame
import math
class ImageInfo :
    def __init__(self, pathImage):
        model = YOLO('yolov8m-seg.pt')
        self.__allNames = model.names
        self.__boxes = model(pathImage)[0].boxes
        self.__classIndices: dict[str, list[int]] = self.__getClassIndicesDict()
    def  __getClassIndicesDict(self):
        res: dict[str, list[int]] = {}
        [self.__updateClassIndices(bi, box, res) for bi, box in enumerate(self.__boxes)] 
        return res 
    def __updateClassIndices(self, bi: int, box, res: dict[str, list[int]]):
        className: str = self.__allNames[box.cls.item()]
        res.setdefault(className, []).append(bi)
    def __getDataFrame(self)-> DataFrame:
        xyxy = self.__boxes.xyxy.cpu().numpy()
        cls = self.__boxes.cls.cpu().numpy()
        conf = self.__boxes.conf.cpu().numpy()
        names = [self.__allNames[c] for c in cls]
        df = DataFrame(xyxy, columns=["xmin", "ymin", "xmax", "ymax"])
        df["name"] = names
        df["confidence"] = conf 
        return df
    def __getDistanceBetween(self,boxInd1: int, boxInd2: int)->float :
        x1_center, y1_center, *_ = self.__boxes[boxInd1].xywhn[0].tolist()
        x2_center, y2_center, *_ = self.__boxes[boxInd2].xywhn[0].tolist()
        return math.hypot(x1_center - x2_center, y1_center - y2_center)
    def __getMinDistance(self, boxIndex: int, boxIndices: list[int]) -> tuple[int, float]:
        res: tuple[int, float] = (boxIndices[0], self.__getDistanceBetween(boxIndex, boxIndices[0] ))
        for bi in boxIndices:
            if (d := self.__getDistanceBetween(boxIndex, bi)) < res[1]:
                res = (bi, d)
        return res        
    def __getBelongingsPersonDict(self):
        belongingIndices = self.boxesClass("suitcase") + self.boxesClass("handbag")
        personIndices = self.boxesClass("person")
        res: dict[int, tuple[int, float]] = {bi: self.__getMinDistance(bi, personIndices)
                                             for bi in belongingIndices}
        return res
    def boxesClass(self, className: str) -> list[int]:
        return self.__classIndices.get(className, [])  
    def boxInfo(self,index: int)-> tuple[float, float, float, float, float, str]:
        box = self.__boxes[index]
        res: list = box.xyxy[0].tolist()
        res.append(box.conf.item())
        res.append(self.__allNames[box.cls.item()])
        return tuple(res)
    def dataFrame(self):
        if not hasattr(self, "__df"):
            self.__df = self.__getDataFrame()
        return self.__df
    def suitcaseHandbagPerson(self, threshold: float) -> dict[int, tuple[int, float]|None]:
        if not hasattr(self, "__belongingPerson"):
            self.__belongingPerson: dict[int, tuple[int, float]] = self.__getBelongingsPersonDict()
        belongPerson: dict[int, tuple[int, float]] = \
        {bi: (pi,d) for bi, (pi, d) in self.__belongingPerson.items()
         if d <= threshold} 
        noBelongPerson:dict[int, None] = \
            {bi: None for bi, (_, d) in self.__belongingPerson.items() 
             if d > threshold}
        return belongPerson | noBelongPerson    
            
               
        