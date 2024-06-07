import random
import time
import subprocess
import json
from huskylib import HuskyLensLibrary

huskylens = HuskyLensLibrary("I2C","", address=0x32)


# def printObjectNicely(obj):
#     count=1

#     #SE FOR UMA LISTA DE OBJETOS
#     if(type(obj)==list):
#         for i in obj:
#             print("\t "+ ("BLOCK_" if i.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(i.__dict__))
#             count+=1
    
#     #SE FOR UM UNICO OBJETO
#     else:
#         #print("\t "+ ("BLOCK_" if obj.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(obj.__dict__))
#         print("(x,y): " + str(obj.x) + ", " + str(obj.y) )
#         #+ " | Width: " + str(obj.width) + " | Height: " + str(obj.height) + " | ID: " + str(obj.ID) + " | Type: " + str(obj.type) + " | Angle: " + str(obj.angle) + " | Confidence: " + str(obj.confidence) + " |")




def eye_tracking():
    # Captura os blocos continuamente
             while True:
                try:
                    block = huskylens.blocks()
                    x, y = block.x, block.y
                    print(x, y)
                    time.sleep(0.1) 
               
                except Exception as e:
                    continue
                except KeyboardInterrupt:
                    print("\nQUITING")
                    quit()

eye_tracking()
