from typing import Iterable
from pandas import DataFrame

def enumerator(values: Iterable[str]) -> dict[str, int]:
    return {s:i for i, s in enumerate(values)}
def columnsMapper(columnsStr: list[str], df: DataFrame)->dict[str, dict[str, int]]:
    return {column: enumerator(df[column].unique()) for column in columnsStr}  
      
def convertX(df:DataFrame, mapper: dict[str, dict[str, int]])-> DataFrame:
  resDict: dict[str, list] = {}
  for column in df:
      resDict[column] = [mapper[column][valueStr] for valueStr in df[column]] if column in mapper else df[column]
  return DataFrame(resDict)    