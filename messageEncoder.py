'''

       Braeden Sowinski

--- Message Variant Encoder ---

  This script takes a message
  and encodes it using a key 
  that is generated from the
  time. Using the four digits
  of time, it goes through the
  characters of the message and
  changes their values. The 
  message can also be decoded.  

-------------------------------
'''

# Imports date library
import datetime

# List of acceptable characters
#charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!- '\"~@#$%^&*(){}[];:<>/\\"

# Scrambled list of acceptable characters
charSet = "1adQqD@(~'jk0s6L5!bvc,?2TViOKPyz[>^:]lR3EnpUS.tGCY-x9w&};%\"huZWIfgMm4HFBrJeNAX78o*<{\\/)$`Ø"

# Test Message
message = "Hello there friend, I am now 18 years old"

# Decode function
def decode(data):
  shift=data["time"].replace(':','')
  index=-1
  decoded=""
  for i in range(len(data["message"])):
    for j in range(len(charSet)):
      if data["message"][i]==charSet[j]:
        index+=1
        if index==4: index=0
        newIndex=(j-int(shift[index]))
        if newIndex<0:newIndex+=len(charSet)
        decoded+=charSet[newIndex]
  decoded=decoded.replace('Ø',' ')
  return {"message":decoded,"date":data["date"],"time":data["time"]}

# Encode Function
def encode(message):
  message=message.replace(' ','Ø')
  date=datetime.date.today()
  time=datetime.datetime.now()
  shift=time.strftime("%H%M")
  index=-1
  encoded=""
  for i in range(len(message)):
    for j in range(len(charSet)):
      if message[i]==charSet[j]:
        index+=1
        if index==4:index=0
        newIndex=j+int(shift[index])
        if newIndex>len(charSet)-1:newIndex-=len(charSet)
        encoded+=charSet[newIndex]
  return {"message":encoded,"date":date.strftime("%y-%m-%d"),"time":time.strftime("%H:%M")}

print(encode(message))
print(decode(encode(message)))
