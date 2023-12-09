#https://www.codingninjas.com/studio/problems/data-type_8357232?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *

def dataTypes(type: str):
   data_size = {
       "Integer":4,
       "Long":8,
       "Float":4,
       "Double":8,
       "Character":1
   }
   if type not in data_size:
       raise ValueError("Invalid data type: {}".format(type))
   return data_size[type]
   c = input()
   print(dataTypes(c))