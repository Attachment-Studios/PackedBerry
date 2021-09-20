# PackedBerry Sub-System 1

import beta
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

	prefix = False
	if msg[0] in prefix_table:
		prefix = True
	
	dev = beta.check(str(message.guild))

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
		dm_user
	]
	return return_table
