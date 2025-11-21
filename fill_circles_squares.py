from typing import Any
import cv2
import yaml
import numpy as np
import math
from common import FULL_IMAGES_TRAIN, LABELS_TRAIN, FULL_IMAGES_VAL, BASE_ROOT, LABELS_VAL, DATA_YAML
import random
CIRCLE = "circle"
SQUARE = "square"
WIDTH = 256
HEIGHT = 256
N_CIRCLES = 30
N_SQUARES = 30
MIN_WIDTH = int(math.floor(WIDTH * 0.05))
MAX_WIDTH = int(math.floor(WIDTH * 0.9))
__circle_label: int = 0
__square_label: int = 1


def update_data_yaml(path: str):
    with open(path) as f:
        data = yaml.safe_load(f)

    update_data_names(data)
    with open(path, "w") as f:
        yaml.safe_dump(data, f)


def update_data_names(data):
    global __circle_label, __square_label
    if "names" in data:
        if CIRCLE not in data["names"].values():
            __circle_label = int(max(data["names"].keys())) + 1
            __square_label = __circle_label + 1
            data["names"][__circle_label] = CIRCLE
            data["names"][__square_label] = SQUARE
        else:
            __circle_label = __getKeyFromUniqueValue(data["names"], "circle")
            __square_label = __getKeyFromUniqueValue(data["names"], "square")
    else:
        data["names"] = {__circle_label: "circle", __square_label: "square"}


def __getKeyFromUniqueValue(dictionary: dict, value: Any) -> Any:
    return next(key for key, val in dictionary.items() if val == value)


def getRandomCircleData() -> tuple[int, int, int]:
    radius = random.randint(MIN_WIDTH // 2, MAX_WIDTH // 2 + 1)
    x_center = random.randint(radius - 1, MAX_WIDTH - radius + 1)
    y_center = random.randint(radius - 1, MAX_WIDTH - radius + 1)
    return (x_center, y_center, radius)
def getRandomSquareData() -> tuple[int, int, int]:
    size = random.randint(MIN_WIDTH, MAX_WIDTH + 1)
    x = random.randint(1, WIDTH - size)
    y = random.randint(1, HEIGHT - size)
    return (x, y, size)

def getAllCirclesData(nCircles: int) -> list[tuple[int, int, int]]:
    return [getRandomCircleData() for _ in range(nCircles)]

def getAllSquareData(nSquares: int) -> list[tuple[int, int, int]]:
    return [getRandomSquareData() for _ in range(nSquares)]


def getCircleImage(x_center: int, y_center: int, radius: int) -> np.array:
    img_arr: np.array = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    cv2.circle(img_arr, (x_center, y_center), radius, (0, 0, 255), -1)
    return img_arr

def getSquareImage(x: int, y: int, size: int) -> np.array:
    img_arr: np.array = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    cv2.rectangle(img_arr, (x, y), (x + size, y + size), (0,0,255), -1)
    return img_arr

def getCircleLabel(x_center: int, y_center: int, radius: int) -> str:
    x = x_center / WIDTH
    y = y_center / HEIGHT
    w = radius * 2 / WIDTH
    h = radius * 2 / HEIGHT
    return f"{__circle_label} {x:.6f} {y:.6f} {w:.6f} {h:.6f}"

def getSquareLabel(x: int, y: int, size: int) -> str:
    x1, x2, y1, y2 = x, x + size, y, y + size
    x_center_norm = ((x1 + x2) / 2) / WIDTH
    y_center_norm = ((y1 + y2) / 2) / HEIGHT
    w_norm = size / WIDTH
    h_norm = size / HEIGHT
    return f"{__square_label} {x_center_norm:.6f} {y_center_norm:.6f} {w_norm:.6f} {h_norm:.6f}"

def saveImageLabel(imagePath: str, labelPath: str, img: np.array, label: str):
    cv2.imwrite(imagePath + '.jpg', img)
    with open(labelPath + '.txt', "w") as f:
        f.write(label)

__img_data: dict = {
    CIRCLE: (getAllCirclesData, getCircleImage, getCircleLabel),
    SQUARE: (getAllSquareData, getSquareImage, getSquareLabel)
}
def saveData(nImages: int, imagePath: str, labelPath, imageType:str):
    getAllData = __img_data[imageType][0]
    getImage = __img_data[imageType][1]
    getLabel = __img_data[imageType][2]
    coordinates: list[tuple[int, int, int]] = getAllData(nImages)
    images: list[np.array] = [getImage(
        cd[0], cd[1], cd[2]) for cd in coordinates]
    labels: list[str] = [getLabel(
        cd[0], cd[1], cd[2]) for cd in coordinates]
    for i in range(nImages):
        saveImageLabel(f"{imagePath}/{imageType}{i}",
                       f"{labelPath}/{imageType}{i}", images[i], labels[i])
def saveCircleSquareData():
    saveData(N_CIRCLES, FULL_IMAGES_TRAIN, LABELS_TRAIN, CIRCLE)
    saveData(int(math.floor(N_CIRCLES * 0.1)), FULL_IMAGES_VAL, LABELS_VAL, CIRCLE)
    saveData(N_SQUARES, FULL_IMAGES_TRAIN, LABELS_TRAIN, SQUARE)
    saveData(int(math.floor(N_SQUARES * 0.1)), FULL_IMAGES_VAL, LABELS_VAL, SQUARE)

update_data_yaml(f"{BASE_ROOT}/{DATA_YAML}")
saveCircleSquareData()

