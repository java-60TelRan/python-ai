from unittest import TestCase, main
from pandas import DataFrame
from converter import enumerator, columnsMapper, convertX
class TestConverter(TestCase):
    def setUp(self):
        self.df = DataFrame(({
            "Company":['Toyota','Toyota','Hundai', 'Hundai', 'Hundai' ],
            "Model": ['Camry', 'Corolla', 'i10', 'Elantra', 'Kona']
            }))
        self.mapper = columnsMapper(["Company","Model"], self.df) 
    def test_enumerator(self):
        expected = {
            'Toyota': 0,
            'Hundai': 1
        } 
        actual = enumerator(self.df['Company'].unique())  
        self.assertEqual(expected, actual) 
    def test_columnsMapper(self) :
        actual: dict[str, dict[str, int]] =columnsMapper(["Company"], self.df) 
        expected:dict[str, dict[str, int]] = {
            "Company":{"Toyota":0, "Hundai":1}
            } 
        self.assertEqual(expected, actual) 
    def test_converterX(self) :
        dfConverter = convertX(self.df,self.mapper)
        actualDict = dfConverter.to_dict(orient="list")
        expectedDict = {"Company":[0,0,1,1,1], "Model": [0, 1, 2, 3, 4]}
        self.assertEqual(expectedDict, actualDict)   
if __name__ == '__main__' :
    main()
       