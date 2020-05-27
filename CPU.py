#!/usr/bin/env python
import psutil
  
# This code is contributed by Neelam Yadav 
# gives a single float value
print(float(psutil.cpu_percent()))
# gives an object with many fields
print(psutil.virtual_memory())
# you can convert that object to a dictionary 
dict_ram = (dict(psutil.virtual_memory()._asdict()))
print("Used RAM: ",float(dict_ram['used'])/1000000,"GB")
