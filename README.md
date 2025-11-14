# HW#33 Definition
## Write class ImageInfo  with  the following methods
### constructor taking path to image
note: model "yolov8m-seg.pt" should be used
### boxesClass method
#### takes class name as string
#### returns box indices matching the boxes of the given class
### boxInfo method
#### takes box's index
#### returns tuple (xmin, ymin, xmax, ymax, confidence, class name)
### dataFrame method
#### takes nothing
#### returns DataFrame of pandas package as done at Classwork
### suitcaseHandbagPerson method
#### takes threshold of the distance in normalized value [0-1] 
#### returns dictionary, where key is index of suitcase/handbag box and value is tuple (index of a box of matched person, normolized distance [0-1]  between cemters of suitcase/handbag and the person boxes)
note 1: matched person is the one, box of which contains a person with minimal distance among other persons
note 2: if minimal distance exceeds the given threshold the value should be None instead of a tuple
hint: consider the property xywhn of a box, tuple (x_center / image_width, y_center / image_height, box_width / image_width, box_height / image_height)
## Write tests on any image (the image of CW may be considered)
note : test of this method doesn't checks distance value but only the box index or None
