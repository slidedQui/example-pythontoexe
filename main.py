import os
file = open("saludo.txt", "w")
file.write("Hello World, From Exe File" + os.linesep)
file.close()