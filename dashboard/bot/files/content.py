with open('C://Users/Harsh/Desktop/healthcare/dashboard/bot/files/chats.txt') as f:
 	content = f.readlines()

with open('C://Users/Harsh/Desktop/healthcare/dashboard/bot/files/data.txt') as f:
	content = f.readlines()

print(content)



f = open("C://Users/Harsh/Desktop/healthcare/dashboard/bot/files/op.txt", "a+")
for x in content:
	f.write(x)
	f.write("\n")
f.close()