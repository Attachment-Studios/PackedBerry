# PackedBerry Sub-System 1

import random
import os

def protocol(client, message, prefix_table):
	msg = message.content.lower().split(" ")
	_msg = message.content.split(" ")

	cmd = ""

	try:
		cmd = msg[1]
	except:
		pass

	out = ""
	dm_user = ""

	ad = False
	reaction_role = False
	role_val = 0

	prefix = False
	if msg[0] in prefix_table:
		prefix = True
	
	if prefix and cmd != "":
		if cmd in ["dm-user", "dm"]:
			try:
				try:
					dm_msg = message.content.replace(f'{_msg[0]} {_msg[1]} {_msg[2]}', '')
					if len(dm_msg.replace(' ', '')) <= 0:
						out = "Need a message."
					else:
						dm_user = "hmmmm"
						out = message.content.replace(f"{_msg[0]} {_msg[1]} {_msg[2]} ", "")
				except:
					out = "Needs a message."
			except:
				out = "Invalid user."
		elif cmd in ["xp", "levels", "level", "messages"]:
			user = str(message.author.id)
			try:
				user = str(msg[2]).replace("<", "").replace("!", "").replace("@", "").replace(">", "")
			except:
				pass
			loc = f"levels/ {user}"
			if os.path.isfile(str(loc)):
				f = open(loc, "r")
				d = f.read()
				f.close()
				dl = d.split("\n")
				xp = int(dl[0])
				l = int(dl[1])
				g = int(dl[2])
				p = xp / g
				if cmd in ["level", "levels"]:
					out = f"<@{user}> is on level {l}"
				elif cmd == "xp":
					out = f"<@{user}>\nXP: {xp}\nGoal: {g}\nCompletion: {p * 100}%"
				else:
					out = f"<@{user}> has {xp} messages."
			else:
				out = "User has no messages under PackedBerry system."
		elif cmd == "welcome":
			if message.author.guild_permissions.administrator:
				if len(msg) < 3:
					out = 'To set welcome channel type:\n`<prefix> welcome channel <channel>`\n\nFor setting welcome message type:\n`<prefix> welcome message <message>`\n\nTo give a default role on joining type:\n`<prefix> welcome role <role>`\n\nFor disabling type:\n`<prefix> welcome disable`\n\nTIP: While setting the message, `<server>` if in the message converts into server name and `<user>` into user ping.'
				else:
					if msg[2] == "disable":
						os.path.remove(f'welcome/{message.guild.id}')
						out = "Disabled Welcome Messages."
					elif msg[2] == "channel":
						if len(msg) < 4:
							out = 'You need to provide a channel.'
						else:
							channel = str(msg[3]).replace('<', '').replace('>', '').replace('#', '')
							try:
								channel_id = int(channel)

								m = 'Hello <user>! Welcome to <server>'
								r = ''
								if os.path.isfile(f'welcome/{message.guild.id}'):
									f = open(f'welcome/{message.guild.id}', 'r')
									data = str(f.read())
									f.close()

									d = data.split('\n')
									
									m = str(d[1])
									r = str(d[2])

								nd = str(channel_id) + '\n' + m + '\n' + r

								f = open(f'welcome/{message.guild.id}', 'w')
								f.write(str(nd))
								f.close()

								out = f'Welcome channel set to <#{channel_id}>'
							except:
								out = 'Please provide a valid channel.'
					elif msg[2] == "role":
						if len(msg) < 4:
							out = 'You need to provide a role.'
						else:
							role = str(msg[3]).replace('<', '').replace('>', '').replace('@', '').replace('&', '')
							try:
								role_id = int(role)

								m = ''
								c = ''
								if os.path.isfile(f'welcome/{message.guild.id}'):
									f = open(f'welcome/{message.guild.id}', 'r')
									data = str(f.read())
									f.close()

									d = data.split('\n')
									
									c = str(d[0])
									m = str(d[1])

								nd = c + '\n' + m + '\n' + str(role_id)

								f = open(f'welcome/{message.guild.id}', 'w')
								f.write(str(nd))
								f.close()

								out = f'Deafault role set to <@&{role_id}>'
							except:
								out = 'Please provide a valid role.'
					elif msg[2] == "message":
						if len(msg) < 4:
							out = 'You need to provide a message.'
						else:
							del _msg[0]
							del _msg[0]
							del _msg[0]
							m = " ".join(_msg)
							try:
								c = ''
								r = ''
								if os.path.isfile(f'welcome/{message.guild.id}'):
									f = open(f'welcome/{message.guild.id}', 'r')
									data = str(f.read())
									f.close()

									d = data.split('\n')
									
									c = str(d[0])
									r = str(d[2])

								nd = c + '\n' + m + '\n' + r

								f = open(f'welcome/{message.guild.id}', 'w')
								f.write(str(nd))
								f.close()

								out = f'Welcome message set to {m}'
							except:
								out = 'Error.'
			else:
				out = "Admin permissions needed."
		elif cmd in ["ad", "advertisement"]:
			ad = True
			out = "Ad Delivered."
		elif cmd == "role":
			if message.author.guild_permissions.administrator:
				role = ''
				try:
					_temp = msg[2].replace('<', '').replace('>', '').replace('@', '').replace('&', '')
					try:
						role = int(_temp)
					except:
						role = ''
				except:
					role = ''
				if role == '':
					out = "Error. Role failed to set."
				else:
					out = f"Get <@&{role}> role by reacting with :white_check_mark:"
					reaction_role = True
					role_val = int(role)
			else:
				out = "You don't have admin permissions."
		elif cmd == "scam":
			out = "In Dev"
			try:
				del _msg[0]
				del _msg[0]
				data = ' '.join(_msg)
				if len(data.replace(' ', '')) == 0:
					out = "You need to give data."
				else:
					data = "\n" + data
					sf = open('scam/scam', 'r')
					sd = sf.read()
					sf.close()
					sf = open('scam/scam', 'w')
					sf.write(str(sd) + str(data))
					sf.close()
					out = 'Scam Saved.'
			except:
				out = "You need to give data."
		elif cmd == "tac":
			f = open('legal/TAC/tac.md', 'r')
			out = '**PackedBerry Terms and Conditions**\n\n' + str(f.read()).replace('```', '------------------')
			f.close()
		elif cmd == "coin":
			out = ["Head", "Tails"][random.randint(0, 1)]
		elif cmd == "server":
			try:
				server = client.get_guild(int(msg[2]))
			except:
				server = message.guild
			out = f"""
Server Details

Information Based:
Name: {server.name}
Description: {server.description}
ID: {server.id}
Creation Date: {server.created_at}

Amount Based:
Members: {server.member_count}
All Channels: {len(server.channels)}
Text Channels: {len(server.text_channels)}
Voice Channels: {len(server.voice_channels)}
Stage Channels: {len(server.stage_channels)}
Categories: {len(server.categories)}

Image Stuff:
Icon: {str(server.icon_url)}
Banner: {str(server.banner_url)}
"""
	
	return_table = [
		out,
		dm_user,
		ad,
		reaction_role,
		role_val
	]
	return return_table
