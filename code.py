import os


nextLineIsATimestamp = False
newBlock = False
block = []
formattedLine = None
ts = None

if os.path.exists("new_destination.csv"):
  os.remove("new_destination.csv")
else:
  print("The file does not exist")

writer = open("new_destination.csv", "a")

with open('source.log', 'r') as reader:

  for line in reader:

    formattedLine = ' '.join(line.split())
    formattedLine = formattedLine.replace(" ", ',')
    if '----' in line:
      newBlock = True
      nextLineIsATimestamp = True      
    elif nextLineIsATimestamp:
      nextLineIsATimestamp = False
      # this is a new block, this is a timestamp
      ts = formattedLine
      # reset the state
      newBlock = False
    else:
      block = formattedLine + "," + ts
      writer.write(block)
      writer.write("\n")      
    
    formattedLine = None



writer.close()
