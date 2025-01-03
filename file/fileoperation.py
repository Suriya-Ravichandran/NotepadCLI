import os

def createfile(name):
    file=open(f"{name}","x")
    if(file):
     print("created successfully")
    else:
      print("not created")
    file.close()

def writefile(name,content):
  file=open(f"{name}","a")
  file.write(content)
  if(file):
     print("created and Write successfully")
  else:
    print("error")
  file.close()

def overwrite(name,content):
  file=open(f"{name}","w")
  file.write(content)
  if(file):
     print("OverWrite successfully")
  else:
    print("error")
  file.close()

def read(name):
  file=open(f"{name}","r")
  print(file.read())
  file.close()

def delete(name):
  if os.path.exists(name):
     os.remove(name)
     print("Delete a File successfully")
  else:
    print("The file does not exist")