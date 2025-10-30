from unittest import TestCase, main
from pandas import DataFrame
from converter import enumerator, columnsMapper, convertX
class TestConverter(TestCase):
    def setUp(self):
        self.df = DataFrame(({
            "Company":['Toyota','Toyota','Hundai', 'Hundai', 'Hundai' ],
            "Model": ['Camry', 'Corolla', 'i10', 'Elantra', 'Kona']
            }))
    def test_enumerator(self):
        expected = {
            'Toyota': 0,
            'Hundai': 1
        } 
        actual = enumerator(self.df['Company'].unique())  
        self.assertEqual(expected, actual) 
if __name__ == '__main__' :
    main()
       