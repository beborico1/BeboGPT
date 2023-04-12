lineas_de_nuevo_archivo = []

with open("chat1.txt", "r") as archivo:
    for linea in archivo:
        if "] Luis Rico: " in linea:
            nueva_linea = linea.split("] Luis Rico: ")[1]
            lineas_de_nuevo_archivo.append(nueva_linea)

with open("chat2.txt", "r") as archivo:
    for linea in archivo:
        if "] Luis Rico: " in linea:
            nueva_linea = linea.split("] Luis Rico: ")[1]
            if not "omitido" in linea and not "omitida" in linea and not "Esperando el mensaje. Esto puede tomar tiempo" in linea:
                lineas_de_nuevo_archivo.append(nueva_linea)

with open("chatbot.txt", "w") as archivo:
    for linea in lineas_de_nuevo_archivo[1:250]: # saltandose el primer elemento de la lista
        archivo.write(linea)