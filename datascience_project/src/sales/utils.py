import uuid
#all the helper functions store here.

def generateCode():
  code = uuid.uuid4()
  code_mod = str(code).replace('-','')[:12]
  print(code)
  print(code_mod)
  return code_mod

