from pyrogram import Client, Filters, Emoji
import random
import time
app = Client("session",bot_token="970111231:AAHNo-_KDenyAbaEHgYOruD4ZRWcr-nHB10",api_id=605563,api_hash="7f2c2d12880400b88764b9b304e14e0b")  
@app.on_message(Filters. command('sps'))
def ran(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
   message.reply(random.choice(['Paper', 'Stone','Sessiors']))

@app.on_message(Filters.command('coin'))
def ran(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
   file = open("se.txt","r")
   z = file.readlines()
   file.close()
   for c in z:
    if c == "no":
     message.reply(randon.choice(["Heads","Tails","Tails","Heads","Tails","Heads"]))
    if c == "head":
     message.reply("Heads")
    if c == "tail":
     message.reply("Tails")


@app.on_message(Filters.command('roll'))
def ran(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
   file = open("hack.txt","r")
   z = file.readlines()
   file.close()
   for c in z:
    if c == "no":
     message.reply(random.choice(range(1,7)))
    else:
     file = open("hack.txt","r")
     l = file.readlines()
     file.close()
      for a in l:
        file = open("hack.txt","r")
        b = file.readlines()
        file.close()
        for v in b:
         message.reply(v.text.split(" ")[int(a)])



@app.on_message(Filters.command('droll'))
def ran(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
  message.reply(random.choice(range(1,7)))
  message.reply(random.choice(range(1,7)))
@app.on_message(Filters. command('show'))
def ran(client, message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
   file = open("sure.txt","r")
   z = file.readlines()
   file.close()
   for c in z:
    if c == "no":
     if len(message.text.split(' ')) > 1:
      message.reply("{} cards ".format(message.text.split(' ')[1]) + random.choice(["2","3","4","5","6","7","8","9","10","A","K","Q","J"]) + random.choice([ "♠️","♣️","♥️","♦️" ]))
      message.reply("{} cards ".format(message.text.split(' ')[1]) + random.choice(["2","3","4","5","6","7","8","9","10","A","K","Q","J"]) + random.choice([ "♠️","♣️","♥️","♦️" ]))
      message.reply("{} cards ".format(message.text.split(' ')[1]) + random.choice(["2","3","4","5","6","7","8","9","10","A","K","Q","J"]) + random.choice([ "♠️","♣️","♥️","♦️" ]))
     else:
      message.reply('Correct Usage: /show username')
    else:
     if len(message.text.split(' ')) > 1:
      g = "{} cards ".format(message.text.split(' ')[1]) + random.choice(["2","3","4","5","6","7","8","9","10","A","K","Q","J"]) + random.choice([ "♠️","♣️","♥️","♦️" ])
      m = random.choice(range(1,5))
      if m == 1:
       message.reply(g)
       message.reply("{} cards ".format(message.text.split(' ')[1]) + random.choice(["2","3","4","5","6","7","8","9","10","A","K","Q","J"]) + random.choice([ "♠️","♣️","♥️","♦️" ]))
       message.reply(g)
       with open("sure.txt","w") as file:
        file.write("no")
        file.close()
      if m == 2:
       message.reply(g)
       message.reply(g)
       message.reply("{} cards ".format(message.text.split(' ')[1]) + random.choice(["2","3","4","5","6","7","8","9","10","A","K","Q","J"]) + random.choice([ "♠️","♣️","♥️","♦️" ]))
       with open("sure.txt","w") as file:
        file.write("no")
        file.close()
      if m == 3:
       message.reply("{} cards ".format(message.text.split(' ')[1]) + random.choice(["2","3","4","5","6","7","8","9","10","A","K","Q","J"]) + random.choice([ "♠️","♣️","♥️","♦️" ]))
       message.reply(g)
       message.reply(g)
       with open("sure.txt","w") as file:
        file.write("no")
        file.close()
      if m == 4:
       message.reply(g)
       message.reply(g)
       message.reply(g)
       with open("sure.txt","w") as file:
        file.write("no")
        file.close()
     else:
      message.reply('Correct Usage: /show username')
@app.on_message(Filters. command('leavechat'))
def ran(client,message):
 if message.from_user.id == 491634139:
  if len(message.text.split( )) > 1:
    client.leave_chat(int(message.text.split(' ')[1]))
  else:
    client.leave_chat(message.chat.id)
@app.on_message(Filters. command('cnnn'))
def ran(client,message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
  with open("sure.txt","w") as file:
   file.write("no")
   file.close()
   message.reply("Success off")
@app.on_message(Filters.command('cyyy'))
def ran(client,message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
  with open("sure.txt","w") as file:
   file.write("yes")
   file.close()
   message.reply("Success on")
@app.on_message(Filters.command('statss'))
def ran(client,message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
   file = open("sure.txt","r")
   z = file.readlines()
   file.close()
   for c in z:
    message.reply(c)

#end

@app.on_message(Filters.command('croll'))
def ran(client,message):
 x = client.get_chat_member(message.chat.id , message.from_user.id).status
 if x == "administrator" or x == "creator":
  with open("seq.txt","w") as file:
   file.write(message.reply_to_message.text)
   file.close()
  with open("info.txt","w") as file:
   file.write("1")
   file.close()
  with open("hack.txt","w") as file:
   file.write("yes")
   file.close()
  message.reply("Success " + message.reply_to_message.text)

app.run()

