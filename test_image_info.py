from unittest import TestCase, main

from pandas import DataFrame
from image_info import ImageInfo
class TestImageInfo(TestCase):
    def setUp(self):
        self.imageInfo = ImageInfo("street.jpg")
    def test_boxes_class(self):
        self.assertEqual([2, 3, 4, 5, 6], self.imageInfo.boxesClass("person"))
        self.assertEqual([7, 9], self.imageInfo.boxesClass("suitcase") + self.imageInfo.boxesClass("handbag")) 
        self.assertEqual([0, 8], self.imageInfo.boxesClass("car"))
    def test_box_info(self):
        tuple_exp = (
            1434.1,	1108.2,	2802.4,	2321.8,	0.9, "car"	
        )
        tuple_act = self.imageInfo.boxInfo(0)
        for exp, act in zip(tuple_exp, tuple_act):
            if isinstance(exp, float):
                self.assertAlmostEqual(exp, act, places=1)
            else:
                self.assertEqual(exp, act)    
    def test_data_frame(self) :
        df1: DataFrame = self.imageInfo.dataFrame()
        df2: DataFrame = self.imageInfo.dataFrame()
        self.assertTrue(df1.equals(df2)) 
        self.assertEqual((10, 6), df1.shape)
        self.assertEqual("car",df1["name"][0])
        self.assertAlmostEqual(0.3, df1["confidence"][9],places=1)
    def test_suitcase_handbag_belongings(self):
        belongingsDict = self.imageInfo.suitcaseHandbagPerson(0.1) 
        self.assertEqual(4, belongingsDict[7][0])
        self.assertEqual(4, belongingsDict[9][0])
        self.assertTrue(belongingsDict[7][1] > belongingsDict[9][1] and belongingsDict[7][1] < 0.1)
    def test_handbag_belongings(self) :
        belongingsDict = self.imageInfo.suitcaseHandbagPerson(0.08) 
        self.assertEqual(4, belongingsDict[9][0])  
        self.assertIsNone(belongingsDict[7]) 
    def test_no_belongings(self) :
        belongingsDict = self.imageInfo.suitcaseHandbagPerson(0.05) 
        self.assertIsNone(belongingsDict[7])          
        self.assertIsNone(belongingsDict[9])          
          