import gpt_2_simple as gpt2
import tensorflow as tf

# Asegúrate de haber descargado el modelo "117M" de GPT-2, si aún no lo has hecho.

# Restablecer el gráfico de TensorFlow (solo si estás utilizando TensorFlow 1.x)
if hasattr(tf, 'reset_default_graph'):
    tf.reset_default_graph()

# Crear el modelo
sess = gpt2.start_tf_sess()

# Cargar el modelo desde la carpeta de checkpoint
checkpoint_dir = 'checkpoint'  # Cambia esto al nombre de la carpeta que utilizaste al guardar el modelo
gpt2.load_gpt2(sess, checkpoint_dir=checkpoint_dir)

input_text = ""

# Llama a la función generate() para generar texto a partir del modelo entrenado
generated_text = gpt2.generate(sess,
                               length=1000, # Longitud del texto generado en número de tokens
                               temperature=0.7, # Creatividad del modelo (valores más bajos producirán texto más coherente)
                               prefix=input_text, # El texto de entrada (prompt) que guiará la generación de texto
                               nsamples=1, # Número de muestras de texto generadas
                               batch_size=1, # Tamaño del lote (deja en 1 si no estás seguro)
                               return_as_list=True) # Devuelve el texto generado como una lista

print(generated_text[0])
