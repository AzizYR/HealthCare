from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3

bot = ChatBot('Sheku',tie_breaking_method="random_response")
trainer = ListTrainer(bot)

sheku = pyttsx3.init()
#bot.set_trainer(ListTrainer)


for _file in os.listdir('files'):
	chats = open("files/" + _file , 'r').readlines()

trainer.train(chats)

name = input("Sheku: What is your name?\n")
print("Ask Me Anything:")

while True:
	request = input(name +':')
	response = bot.get_response(request)
	sheku.say(response)
	print("Sheku:",response)
	sheku.runAndWait()
