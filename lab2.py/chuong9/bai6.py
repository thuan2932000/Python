text = ""
while text.lower() != "quit":
 text = input("Please enter 'QUIT' or 'quit' to exit: ")
 if text == "quit":
  print("…exiting program")
 elif text =="QUIT":
   print("…exiting program")
 else:
  print("Unknown compound")