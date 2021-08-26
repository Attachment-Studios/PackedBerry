# PackedBerry System

from better_profanity import profanity
import requests
import random

def get_title(url: str):
	html = requests.get(url).text
	title_separator = html.split("<title>")
	title = title_separator[1].split("</title>")[0]
	return title

vfile = open("data/version", "r")
version = vfile.read()
vfile.close()
hfile = open("data/help", "r")
help_data = hfile.read()
hfile.close()
wfile = open("data/whatsnew", "r")
whatsnew = wfile.read()
wfile.close()

def mute(uid, mute_list, guild_id, mute_server):
	id_match = False
	for elem in mute_list:
		if str(elem) == str(uid):
			id_match = True
			break
	server_match = False
	for elem in mute_server:
		if str(elem) == str(guild_id):
			server_match = True
			break
	if id_match and server_match:
		return True
	else:
		return False

def mod(message):
	msg = message.content.lower()
	return len(msg) - len(profanity.censor(msg, ""))

def out(message, refname, client):
	try:
		msg = message.content.lower().split(" ")

		out = ""
		delete = False

		connectVoice = False
		voiceChannel = ""
		song_url = ""

		calls = refname

		repeat = 1

		mutelist = []
		unmutelist = []
		if msg[0] in refname[1]:
			try:
				if msg[1] == "ver":
					out = version
				elif msg[1] == "whatsnew":
					out = whatsnew
				elif msg[1] == "help":
					try:
						if msg[2] == "detailed":
							_help = open("data/d_help", "r")
						else:
							_help = open("help", "r")
						out = _help.read()
						_help.close()
					except:
						out = help_data
				elif msg[1] == "ping":
					out = f"<@{message.author.id}>"
				elif msg[1] == "sitename":
					try:
						site_url = str(message.content.split(" ")[2])
						try:
							title = get_title(site_url)
						except:
							title = "???"
						out = title
					except:
						out = "Please provide URL."
				elif msg[1] == "vibe":
					try:
						try:
							try:
								voiceChannel = str(message.content).replace( str(message.content.split(" ")[0]) + " " + str(message.content.split(" ")[1]) + " " + str(message.content.split(" ")[2] + " "), "" )
								song_url = str(message.content.split(" ")[2])
								try:
									title = get_title(song_url)
								except:
									title = "???"
								out = "Now vibing on " + title + "(<" + song_url + ">) on voice channel " + voiceChannel + "!!!"
								connectVoice = True
							except:
								out = "Error."
						except:
							out = "Please provide a voice channel to vibe in!"
					except:
						out = "Please provide an url to vibe on!"
				elif msg[1] == "novibe":
					connectVoice = "-"
					out = "Not vibing anymore."
				elif msg[1] == "pausevibe":
					connectVoice = "||"
					out = "Waiting till start vibing again."
				elif msg[1] == "resumevibe":
					connectVoice = ">"
					out = "Resuming vibing again."
				elif msg[1] == "donevibe":
					connectVoice = "<"
					out = "Stopped vibing."
				elif msg[1] == "spam":
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
				elif msg[1] == "call":
					try:
						if str(msg[2]) not in calls[1]:
							calls[1].append(str(msg[2]))
						out = 'Added name option - ' + str(message.content.split(' ')[2]) + '. Now you can use ' + str(message.content.split(' ')[2]) + ' as prefix to start a PackedBerry command.'
					except:
						all_names = "```"
						called = []
						for name in calls[1]:
							if name not in called:
								all_names = all_names + '\n' + str(name)
								called.append(name)
						all_names = all_names + '\n```'
						out = str(all_names)
				elif msg[1] == "nocall":
					try:
						if str(msg[2]) in calls[1]:
							calls[1].remove(str(msg[2]))
						if str(msg[2]) in calls[0]:
							out = 'Can not remove system default names!'
						else:
							out = 'Removed name option - ' + str(message.content.split(' ')[2]) + '. Now you can not use ' + str(message.content.split(' ')[2]) + ' as prefix to start a PackedBerry command.'
						for name in calls[0]:
							if name not in calls[1]:
								calls[1].append(name)
					except:
						out = 'Please provide a name!'
				elif msg[1] == "mute":
					try:
						mutelist.append(str(msg[2]).replace('<', '').replace('>', '').replace('@!', ''))
						out = f'{msg[2]} was muted.'
					except:
						out = 'Please provide user to mute.'
				elif msg[1] == "unmute":
					try:
						unmutelist.append(str(msg[2]).replace('<', '').replace('>', '').replace('@!', ''))
						out = f'{msg[2]} was unmuted.'
					except:
						out = 'Please provide user to unmute.'
				elif msg[1] == "img":
					try:
						out = f"https://picsum.photos/seed/{ str(msg[2]) }/1920/1080"
					except:
						out = f"https://picsum.photos/seed/{ random.randint(1, 1000000) }/1920/1080"
			except:
				out = "Yes!?"
		else:
			"""if mod(message) > 3:
				delete = True
				if mod(message) > 4:
					if mod(message) > 5:
						if mod(message) > 6:
							out = f"<@{message.author.id}> Control! Control! Control! You need to be peaceful!"
						else:
							out = f"<@{message.author.id}> Don't make others hate you!"
					else:
						out = f"<@{message.author.id}> Buddy! Stay cool!"
				else:
					out = f"<@{message.author.id}> Your language seems to be a bit rude. I would suggest you to calm down."
			else:
				delete = False"""
			pass
		if out == "":
			return [False, out, delete, connectVoice, voiceChannel, song_url, repeat, calls, mutelist, unmutelist]
		else:
			return [True, out, delete, connectVoice, voiceChannel, song_url, repeat, calls, mutelist, unmutelist]
	except:
		pass

