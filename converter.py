from typing import Iterable
import pandas as pd

def enumerator(values: Iterable[str]) -> dict[str, int]:
    return {s:i for i, s in enumerate(values)}
def columnsMapper(columnsStr: list[str], df: pd.DataFrame)->dict[str, dict[str, int]]:
  res: dict[str, dict[str, int]] = {}
  for column in columnsStr:
      res[column] = enumerator(df[column].unique())
  return res    
      
def convertX(df:pd.DataFrame, mapper: dict[str, dict[str, int]])-> pd.DataFrame:
  resDict: dict[str, list] = {}
  for column in df:
      resDict[column] = []
      if column in mapper:
          for valueStr in df[column]:
              resDict[column].append(mapper[column][valueStr])
      else: resDict[column] = df[column]
  return pd.DataFrame(resDict)    