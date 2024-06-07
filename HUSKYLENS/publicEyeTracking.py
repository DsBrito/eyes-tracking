# import random
# import time
# import subprocess
# import json
# from huskylib import HuskyLensLibrary
# # from huskylensPythonLibrary import HuskyLensLibrary

# # hl = HuskyLensLibrary("SERIAL", "/dev/ttyUSB1", 3000000)
# huskylens = HuskyLensLibrary("I2C","", address=0x32)





# # comando = "ls -l"
# # processo = subprocess.run(comando, shell=True, check=True, text=True, capture_output=True)
# # print(processo.stdout)
# #rostopic pub /eye_position std_msgs/String "x:$(python -c 'print(obj.x)') y:$(python -c 'print(obj.y)')" --once


# def printObjectNicely(obj):
#     count=1

#     #SE FOR UMA LISTA DE OBJETOS
#     if(type(obj)==list):
#         for i in obj:
#            # print("\t "+ ("BLOCK_" if i.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(i.__dict__))
#             count+=1
    
#     #SE FOR UM UNICO OBJETO
#     else:
#          print('oi')
#          #print("(x,y): " + str(obj.x) + ", " + str(obj.y) )
#          command = "rostopic pub /eye_position std_msgs/String \"x:$('(str(obj.x))') y:$('print(str(obj.y))')\""
#          process = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
#          print(process.stdout)
#         #print("\t "+ ("BLOCK_" if obj.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(obj.__dict__))
#         #print("(x,y): " + str(obj.x) + ", " + str(obj.y) )
#         #+ " | Width: " + str(obj.width) + " | Height: " + str(obj.height) + " | ID: " + str(obj.ID) + " | Type: " + str(obj.type) + " | Angle: " + str(obj.angle) + " | Confidence: " + str(obj.confidence) + " |")




# def eye_tracking():
#     # Captura os blocos continuamente
#              while True:
#                 try:
#                 # Captura os blocos continuamente
#                     printObjectNicely(huskylens.blocks())
#                     time.sleep(0.1)  # Espera um curto perÃ­odo para nÃ£o sobrecarregar o sistema
               
#                 except Exception as e:
#                     continue
#                 except KeyboardInterrupt:
#                     print("\nQUITING")
#                     quit()


# eye_tracking()



# import time
# import subprocess
# import json
# from huskylib import HuskyLensLibrary

# huskylens = HuskyLensLibrary("I2C", "", address=0x32)

# def printObjectNicely(obj):
#     count = 1

#     if type(obj) == list:
#         for i in obj:
#             print("\t " + ("BLOCK_" if i.type == "BLOCK" else "ARROW_") + str(count) + " : " + json.dumps(i.__dict__))
#             count += 1
#     else:
#         print("(x,y): " + str(obj.x) + ", " + str(obj.y))

# def publish_eye_position(x, y):
#     # Formatar os valores de x e y no formato desejado para o ROS
#     mensagem = f"x:{x} y:{y}"

#     # Comando para publicar a mensagem no tópico "/eye_position"
#     comando = f"rostopic pub /eye_position std_msgs/String '{mensagem}' --once"

#     # Executar o comando no terminal
#     subprocess.run(comando, shell=True)

# def eye_tracking():
#     while True:
#         try:
#             # Captura os blocos continuamente
#             blocks = huskylens.blocks()
#             for block in blocks:
#                 x, y = block.x, block.y
#                 printObjectNicely(block)
#                 publish_eye_position(x, y)
#             time.sleep(0.1)  # Espera um curto período para não sobrecarregar o sistema

#         except Exception as e:
#             continue
#         except KeyboardInterrupt:
#             print("\nQUITING")
#             quit()

# eye_tracking()



import random
import time
import subprocess
import json
from huskylib import HuskyLensLibrary

huskylens = HuskyLensLibrary("I2C","", address=0x32)




def eye_tracking():
    # Captura os blocos continuamente
             while True:
                try:
                    block = huskylens.blocks()

                    x, y = block.x, block.y
                    print(x, y)
                    command = "rostopic pub /eye_position std_msgs/String \"x:{} y:{}\" --once".format(x, y)
                    process = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
                    print(process.stdout)
                    time.sleep(0.1) 
               
                except Exception as e:
                    continue
                except KeyboardInterrupt:
                    print("\nQUITING")
                    quit()


eye_tracking()
