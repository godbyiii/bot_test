import random
import time

#8 Ball
eight_ball = ['It is certain', ' It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
              'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
              'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
              'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no',
              'Outlook not so good', 'Very doubtful', 'Concentrate and ask again... just kidding.  NO.']

five_ws = ['who', 'what', 'when', 'where', 'why', 'how']

bot_tags = ['@elysia', '@ely']

def create_response(sentence, name, parse):
	msg = {}
	if any(word in sentence for word in bot_tags):
		if "?" in sentence:
			if any(word in sentence for word in five_ws):
				msg = "Your w words confused me."
			elif " or " in sentence:
				msg = "Picking options is difficult.  Ill get back to you on that."
			else:
				num = random.randint(0, (len(eight_ball)-1))
				msg = eight_ball[num]
	if "save" in sentence:
		f = open('saved.txt','r')
		message = f.read()
		msg =message
		f.close()
	time.sleep(1)
	return msg
