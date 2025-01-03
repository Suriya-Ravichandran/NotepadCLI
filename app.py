from file import fileoperation
import os
import sys

sys.stdin = None  # or sys.stdin = open("somefile.txt")



while True:
  print("Hello this is simple Word application")
  print("Press 1 to Create a file\nPress 2 to write a file\nPress 3 to Overwrite a File\nPress 4 to Read a file\nPress 5 to Delete a file\nPress 0 to Exit the App")
  choice=int(input("Enter your Choice: "))
  if(choice==1):
    name=str(input("Enter file name: "))
    fileoperation.createfile(name)

  elif(choice == 2):
      name = input("Enter file name: ")  # Get the file name
      print("Enter/Paste your content. Ctrl-D or Ctrl-Z (windows) to save it.")
      
      contents = []  # List to store all the lines entered by the user
      while True:
          try:
              line = input()  # Read a line of input
          except EOFError:  # Break on EOF (Ctrl-D or Ctrl-Z)
              break
          contents.append(line)  # Append the line to the contents list

      # Join all the lines in contents into a single string
      newcontent = "\n".join(contents)

      # Assuming fileoperation.writefile is a function you have that handles file writing
      fileoperation.writefile(name, newcontent)


  elif(choice==3):
    name = input("Enter file name: ")  # Get the file name
    if os.path.exists(name):
      fileoperation.read(name)
      print("Press 1 to Edit, Press 2 Exit")
      choice=int(input("Enter your Choice"))
      if(choice==1):
        print("Enter/Paste your content. Ctrl-D or Ctrl-Z (windows) to save it.")
          
        contents = []  # List to store all the lines entered by the user
        while True:
            try:
                line = input()  # Read a line of input
            except EOFError:  # Break on EOF (Ctrl-D or Ctrl-Z)
                break
            contents.append(line)  # Append the line to the contents list

        # Join all the lines in contents into a single string
        
        newcontent = "\n".join(contents)

        # Assuming fileoperation.writefile is a function you have that handles file writing
        fileoperation.overwrite(name, newcontent)
      elif(choice==2):
         print("Exit....")

  elif(choice==4):
    name=str(input("Enter file name: "))
    fileoperation.read(name)

  elif(choice==5):
    name=str(input("Enter file name: "))
    fileoperation.delete(name)

  elif(choice==0):
      print("Existing.....!")
      break
  
  else:
    print("Invaild Option...!")

  