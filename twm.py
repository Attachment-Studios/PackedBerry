# PackedBerry Talk With Me

import random
from fun import whitespace

def twm(client, message, prefix):
	out = ""

	_msg = message.content.split(" ")
	msg = message.content.lower().split(" ")

	cmd = msg[1] if len(msg) > 1 else ""

	repeat = 1

	do_prefix = msg[0] in prefix

	if do_prefix:
		if cmd in ["version", "ver"]:
			ver_file = open("data/version", "r")
			out = str(ver_file.read())
			ver_file.close()
		elif cmd in ['hi', 'hello', 'yo']:
			out = "Hello :D"
		elif cmd in ['whatsnew', 'wn']:
			wnf = open('data/whatsnew', 'r')
			out = str(wnf.read())
			wnf.close()
		elif cmd == "license":
			lf = open('legal/Licenses/ASBL.md', 'r')
			out = '```md\n' + str(lf.read()) + '\n```'
			lf.close()
		elif cmd in ["credits", "credit"]:
			cf = open('legal/Credits/Main Credits.md')
			out = str(cf.read()).replace('#', '')
			cf.close()
		elif cmd == "help":
			if len(msg) < 3:
				help_file = open('dm system/help', 'r')
				help_data = help_file.read()
				help_file.close()
				out = str(help_data)
			else:
				help_file = open('dm system/__help__', 'r')
				help_data = help_file.read().split("***")
				help_data.remove("")
				help_file.close()
				for _ in help_data:
					list_ = _.split("\n")
					list_.remove('')
					if len(list_) > 0:
						if list_[0] == msg[2]:
							out = str(_)
							break
				if out == "":
					out = "```yml\n*unavailable```"
		elif cmd == "ping":
			out = '<@' + str(message.author.id) + '>'
		elif cmd in ["img", "image", "pic", "photo", "picsum"]:
			try:
				out = f"https://picsum.photos/seed/{ str(msg[2]) }/1920/1080"
			except:
				out = f"https://picsum.photos/seed/{ random.randint(1, 1000000) }/1920/1080"
		elif cmd == 'random-number':
			try:
				try:
					out = str(random.randint(int(msg[2]), int(msg[3])))
				except:
					out = str(random.randint(0, int(msg[2])))
			except:
				out = str(random.randint(0, 1000000000))
		elif cmd == 'choose':
			if len(msg) < 3:
				out = 'Please provide some options to choose from.'
			else:
				choices = []
				for i in _msg:
					if _msg.index(i) in [ 0, 1 ]:
						pass
					else:
						choices.append(i)			
				out = str(choices[random.randint(0, int(len(choices) - 1))])
		elif cmd in ['random-rearrangement', 'nag-a-ram', 'anagram', 'random-rearrange']:
			try:
				if whitespace(msg[2]):
					out = 'Needs something to randomly rearrange.'
				else:
					real_text = _msg[2]
					id_string = ''
					
					for _ in range(len(real_text)):
						random_number = random.randint(0, len(real_text) - 1)
						while str(random_number) in id_string:
							random_number = random.randint(0, len(real_text) - 1)
						id_string += ' ' + str(random_number)
					
					corrected_list = []

					for i in ((id_string.split(' '))):
						if i == '' or i == None:
							pass
						else:
							corrected_list.append(int(i))
					
					new_string = ''
					for n in corrected_list:
						new_string += str(real_text[n])
					
					out = str(new_string)
			except:
				out = 'Needs something to randomly rearrange.'
		elif cmd == "spam":
			try:
				try:
					if int(msg[2]) <= 25:
						spam_text = ""
						try:
							spam_text = str(message.content).replace( str(message.content.split(" ")[0]) + " " + str(message.content.split(" ")[1]) + " " + str(message.content.split(" ")[2] + " "), "" )
						except:
							spam_text = ""
						if spam_text.replace(" ", "") == '':
							out = "Please provide text to spam."
						else:
							out = spam_text
							repeat = int(msg[2])
					else:
						out = "Spam amount limit is 0 to 25 only."
				except:
					out = "Spam amount should be a number."
			except:
				out = "Please specify an amount to spam."
		else:
			if cmd == "":
				out = "Yes!?"
			else:
				out = "If you think that is a command.\n```diff\n-> Your thought is arguable. <-\n```"
	else:
		out = "Hmmmmmmmmmmm..."

	if message.content.lower() == "ping":
		out = "pong"
	if message.content.lower() == "pong":
		out = "ping"
	
	return_list = [
		out,
		repeat
	]
	return return_list
