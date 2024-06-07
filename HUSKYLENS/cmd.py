



import subprocess

comando = "rostopic list"
processo = subprocess.run(comando, shell=True, check=True, text=True, capture_output=True)
print(processo.stdout)


