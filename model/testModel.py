import tflite_runtime.interpreter as tflite
import numpy as np
import sys

arg = sys.argv

items = arg[1].split('_')[0].split(',')
users = arg[1].split('_')[1].split(',')

items = [eval(i) for i in items]
users = [eval(i) for i in users]

interpreter = tflite.Interpreter(model_path='convertedModel_MLP.tflite')

interpreter.allocate_tensors()
tensor_input = interpreter.get_input_details()
tensor_output = interpreter.get_output_details()

idxItem = tensor_input[0]['index']
idxUser = tensor_input[1]['index']
idxOut = tensor_output[0]['index']

reponse = ""

outputs = {}
for i in range(len(users)):

	item = np.array([items[i]], dtype=np.int32).reshape(1,1)
	user = np.array([users[i]], dtype=np.int32).reshape(1,1)

	interpreter.set_tensor(idxItem, item)
	interpreter.set_tensor(idxUser, user)
	interpreter.invoke()

	out = interpreter.get_tensor(idxOut)
	outputs[items[i]] = out[0][0]

grades = dict(sorted(outputs.items(), key= lambda item: item[1], reverse=True))
liste = list(grades.keys())[:10]
liste = [str(i) for i in liste]
print(",".join(liste))
