!pip install gpt-2-simple  # Instalar la biblioteca "gpt-2-simple"

import gpt_2_simple as gpt2

# Descargar el modelo "117M" de GPT-2 (esto solo se necesita hacer una vez)
gpt2.download_gpt2(model_name="117M")

# Crear el modelo
sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              "chat.txt",  # Archivo de texto con datos de entrenamiento
              model_name="117M",
              steps=1000)  # Número de pasos de entrenamiento

# Generar texto con el modelo
gpt2.generate(sess, length=1000)