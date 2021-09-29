# PackedBerry System

import requests
import random
import os

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
				if msg[1] in ["ver", "version"]:
					out = version
				elif msg[1] in ["whatsnew", "wn"]:
					out = whatsnew
				elif msg[1] == "help":
					if len(msg) < 3:
						help_file = open('data/help', 'r')
						help_data = help_file.read()
						help_file.close()
						out = str(help_data)
					else:
						help_file = open('data/__help__', 'r')
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
					if str(message.guild.id) in os.listdir('no-spam'):
						out = "You can not use `spam` command in this server. To enable it type `<prefix> set-spam on`. Note by default if already wasn't set to, then spam max limit is 25. Be careful."
					else:
						try:
							try:
								try:
									sf = open(f'set-spam/{message.guild.id}', 'r')
									spam_limit = int(sf.read())
									sf.close()
								except:
									spam_limit = 25
								if int(msg[2]) <= spam_limit:
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
									out = f"Spam amount limit is 0 to {spam_limit} only."
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
						if message.author.guild_permissions.administrator:
							id = str(msg[2]).replace('<', '').replace('>', '').replace('!', '').replace('@', '')
							if id == str(781701773713997824):
								out = ["Dare you talk to my creator like that again. :rage:", "You can not mute a god.", "This is an action of Violence against PackedBerry."][random.randint(0, 2)]
							elif id == str(message.author.id):
								out = 'Are you serious or just want to punish yourself?'
							else:
								mutelist.append(str(msg[2]).replace('<', '').replace('>', '').replace('!', '').replace('@', ''))
								out = f'{msg[2]} was muted.'
						else:
							out = 'YOOOOOOOOOOOOOOOOLLLLLLLLlllll! You Not The Admin!'
					except:
						out = 'Please provide user to mute.'
				elif msg[1] == "unmute":
					try:
						if message.author.guild_permissions.administrator:
							unmutelist.append(str(msg[2]).replace('<', '').replace('>', '').replace('!', '').replace('@', ''))
							out = f'{msg[2]} was unmuted.'
						else:
							out = 'YOOOOOOOOOOOOOOOOLLLLLLLLlllll! You Not The Admin!'
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
			pass
		return_value = [
				not(out == ""),
				out,
				delete,
				connectVoice,
				voiceChannel,
				song_url,
				repeat,
				calls,
				mutelist,
				unmutelist
			]
		return return_value
	except:
		pass

