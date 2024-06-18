from app.dev.generate import Generate
from app.dev.generate2 import Generate as gt

# model = Generate('aya:35b', "qu'el est mon prenom ?", "/home/useria/Documents/pytestLLM/app/mem.txt", "/home/useria/Documents/pytestLLM/app/mem.txt")
# print(model.ans())

model2 = gt('aya:35b', "alors quel est mon prénom ?")
print(model2.ans())