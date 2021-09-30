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
	do_setup = False
	announce_cs = False
	sfr = False

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
		elif cmd in ["update", "setup"]:
			if message.author.guild_permissions.administrator:
				do_setup = True
				out = "Updating Major PackedBerry Stuff!"
			else:
				out = "Admin Permissions needed."
		elif cmd == "set-spam":
			if message.author.guild_permissions.administrator:
				if len(msg) < 3:
					out = 'This command is to set options for spam.\n\nTo disable spam type:\n`<prefix> set-spam off`\n\nTo enable it type:\n`<prefix> set-spam on`\n\nTo reset it, type:\n`<prefix> set-spam reset`\n\nTo set spam limits type:\n`<prefix> set-spam limit <limit>`'
				else:
					if msg[2] == "off":
						f = open(f'no-spam/{message.guild.id}', 'w')
						f.write('This server has spam disabled.')
						f.close()
						out = "Spam is now turned off."
					elif msg[2] == "on":
						if os.path.isfile(f'no-spam/{message.guild.id}'):
							os.remove(f'no-spam/{message.guild.id}')
							out = "Spam is now turned on."
						else:
							out = "Spam is already on."
					elif msg[2] == "reset":
						if os.path.isfile(f'no-spam/{message.guild.id}'):
							os.remove(f'no-spam/{message.guild.id}')
						f = open(f'set-spam/{message.guild.id}', 'w')
						f.write('25')
						f.close()
						out = "Spam options reset."
					elif msg[2] == "limit":
						try:
							lim = int(msg[3])
							f = open(f'set-spam/{message.guild.id}', 'w')
							f.write(f'{lim}')
							f.close()
							out = f"Limit set to {lim}. Make sure that spam is on by typing `<prefix> set-spam on` or `spam` won't work."
						except Exception as e:
							print(e)
							out = "Limit should be a number."
					else:
						out = 'This command is to set options for spam.\n\nTo disable spam type:\n`<prefix> set-spam off`\n\nTo enable it type:\n`<prefix> set-spam on`\n\nTo reset it, type:\n`<prefix> set-spam reset`\n\nTo set spam limits type:\n`<prefix> set-spam limit <limit>`'
			else:
				out = "You don't have admin permissions."
		elif cmd == "cross-server":
			if message.author.guild_permissions.administrator:
				if len(msg) < 3:
					out = "Cross Server Channels are channels that send message across all servers connected with the facility.\n\nTo remove cross server channel type:\n`<prefix> cross-server off`\n\n To set a cross server channel type:\n`<prefix> cross-server <channel>`"
				else:
					if msg[2] == "off":
						try:
							if os.path.isfile(f'cserver/{message.guild.id}'):
								announce_cs = f'**{message.guild}** disconnected from Cross-Server chat.'
							os.remove(f'cserver/{message.guild.id}')
							out = 'Cross server feature has been disabled now.'
						except:
							out = 'Cross server feature was already disabled.'
					else:
						channel = msg[2]
						try:
							c_id = int(channel.replace('<', '').replace('>', '').replace('#', ''))
							f = open(f'cserver/{message.guild.id}', 'w')
							f.write(str(c_id))
							f.close()
							out = f'Cross server channel set to <#{c_id}>.'
							announce_cs = f'**{message.guild}** is now connected to Cross-Server chat.'
						except:
							out = 'Channel should be valid!'
			else:
				out = 'Admin permissions needed.'
		elif cmd == "latency":
			out = str(f'Ping: {float(int(float(client.latency) * 100000) / 100)} ms')
		elif cmd == "welcome":
			if message.author.guild_permissions.administrator:
				if len(msg) < 3:
					out = 'To set welcome channel type:\n`<prefix> welcome channel <channel>`\n\nFor setting welcome message type:\n`<prefix> welcome message <message>`\n\nTo give a default role on joining type:\n`<prefix> welcome role <role>`\n\nFor disabling type:\n`<prefix> welcome disable`\n\nTIP: While setting the message, `<server>` if in the message converts into server name and `<user>` into user ping.'
				else:
					if msg[2] == "disable":
						if os.path.isfile(f'welcome/{message.guild.id}'):
							os.remove(f'welcome/{message.guild.id}')
							out = "Welcome Messages have been reset."
						else:
							out = "No Welcome message data."
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
		elif cmd == "quote":
			del _msg[0]
			del _msg[0]
			qm = " ".join(_msg)
			f = open('quotes/q', 'r')
			d = str(f.read())
			l = d.split('\n')
			f.close()
			if qm.replace(' ', '') == "":
				if len(l) < 2:
					out = 'No quotes available.'
				else:
					out = str(l[random.randint(1, len(l) - 1)]).replace('\\n', '\n')
			else:
				f = open('quotes/q', 'w')
				f.write(d + '\n*' + qm.replace('**', '12341234').replace('*', '').replace('12341234', '**') + '*\\n__~' + str(message.author.name) + '__')
				f.close()
				out = 'Quote saved.'
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
		role_val,
		do_setup,
		announce_cs,
		sfr
	]
	return return_table
