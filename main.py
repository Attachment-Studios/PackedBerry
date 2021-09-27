# PackedBerry

print("System Started")

import os
import discord
import server
import system
import storage
import nacl
import requests
import fun
import sub1
import twm
import pb_cmd
import threading
import pytube
import random
import better_profanity

def text_filter(text:str):
	pf = better_profanity.profanity
	words = text.split(' ')
	filtered = pf.censor(text, '#')
	_ = filtered.split(' ')

	filtered_words = []
	for i in range(len(_)):
		word = _[i]
		if _[i] == words[i]:
			pass
		else:
			word = _[i][0] * len(words[i])
		filtered_words.append('*' + word + '*')

	return [pf.contains_profanity(text), ' '.join(filtered_words)]

def get_title(url: str):
	html = requests.get(url).text
	title_separator = html.split("<title>")
	title = title_separator[1].split("</title>")[0]
	return title

def advertisement():
	adf = open('scam/scam', 'r')
	adl = adf.read().split('\n')
	ad = adl[random.randint(0, len(adl) - 1)]
	ad = str(ad)
	adf.close()
	return ad

def show_ad(id):
	f = open('no-ads/na', 'r')
	d = str(f.read())
	f.close()

	l = d.split('\n')
	if str(id) in l:
		return False
	else:
		return True

async def reply(stop, ad, ctx, msg):
	message = msg
	embed = None
	m = None
	try:
		if "694131271776862259" in ctx.content:
			embed = discord.Embed(
				color = 0x2f3136,
				title = "**`  X  T  O  P  Y  !  `**",
				description = "**`   F   A   W   K   !   `**"
			)
			user = await client.fetch_user(694131271776862259)
			image = user.avatar_url
			embed.set_image(url=image)
			m = await ctx.channel.send(embed = embed)
			if stop:
				return m, embed
	except Exception as e:
		print(e)
	try:
		if "781701773713997824" in ctx.content:
			embed = discord.Embed(
				color = 0x2f3136,
				title = "**`    A    D    I    T    Y    A    !    `**"
			)
			user = await client.fetch_user(781701773713997824)
			image = user.avatar_url
			embed.set_image(url=image)
			m = await ctx.channel.send(embed = embed)
			if stop:
				return m, embed
	except Exception as e:
		print(e)
	try:
		if len(msg) > 1000:
			f = open("temp/message.md", 'w')
			f.write(msg)
			f.close()

			file = discord.File("temp/message.md")
			embed = discord.Embed(
				color = 0xcbb48b,
				title = "PackedBerry!",
				description = "PackedBerry is more than a simple Discord bot."
			)
			embed.set_thumbnail(url="https://github.com/Attachment-Studios/PackedBerry/blob/master/PackedBerry.png?raw=true")
			embed.add_field(
				name = str(pb_cmd.cmd_key(ctx.content.lower())),
				value = "All Content In The Attachment."
			)
			m = await ctx.channel.send(embed = embed, file = file)
			return m, embed
	except Exception as e:
		print(e)
	try:
		if ad == False:
			if not(pb_cmd.emb_check(ctx.content.lower())):
				m = await ctx.channel.send(message)
			else:
				embed = discord.Embed(
					color = 0xcbb48b,
					title = "PackedBerry!",
					description = "PackedBerry is more than a simple Discord bot."
				)
				embed.set_thumbnail(url="https://github.com/Attachment-Studios/PackedBerry/blob/master/PackedBerry.png?raw=true")
				embed.add_field(
					name = str(pb_cmd.cmd_key(ctx.content.lower())),
					value = message
				)
				m = await ctx.channel.send(embed = embed)
				if show_ad(ctx.author.id):
					if random.randint(0, 7) == 1:
						em = discord.Embed(
							color = 0xcbb48b,
							title = "PackedBerry!",
							description = "PackedBerry is more than a simple Discord bot."
						)
						em.set_thumbnail(url="https://github.com/Attachment-Studios/PackedBerry/blob/master/PackedBerry.png?raw=true")
						em.set_image(url="https://github.com/Attachment-Studios/PackedBerry/blob/master/Social.png?raw=true")
						em.add_field(
							name = str('Like PackedBerry?'),
							value = 'Vote For PackedBerry On DiscordBotList.com - https://discord.ly/packedberry'
						)
						await ctx.channel.send(embed = em)
					if random.randint(0, 7) < 3:
						_ad = advertisement()
						emb = discord.Embed(
							color = 0xcbb48b,
							title = "PackedBerry!",
							description = "PackedBerry is more than a simple Discord bot."
						)
						emb.set_thumbnail(url="https://github.com/Attachment-Studios/PackedBerry/blob/master/PackedBerry.png?raw=true")
						emb.add_field(
							name = str('Advertisement'),
							value = _ad
						)
						await ctx.channel.send(embed = emb)
				print(f"\033[38;2;0;255;0m\033[1m\033[3mReply\033[0m: {ctx.author}: \033[38;2;0;255;255m\033[1m\033[3m{pb_cmd.cmd_key(ctx.content.lower())}\033[0m")
		else:
			_ad = advertisement()
			emb = discord.Embed(
				color = 0xcbb48b,
				title = "PackedBerry!",
				description = "PackedBerry is more than a simple Discord bot."
			)
			emb.set_thumbnail(url="https://github.com/Attachment-Studios/PackedBerry/blob/master/PackedBerry.png?raw=true")
			emb.add_field(
				name = str('Advertisement'),
				value = _ad
			)
			await ctx.channel.send(embed = emb)
	except Exception as e:
		print(e)
	return m, embed

ls = [
	0, # xp
	1, # level
	50, # goal
	0, # author id
	"levels/",
	"f"
]

async def level_system(msg):
	ls[3] = str(msg.author.id)
	if os.path.isfile(str(f"{ls[4]} {ls[3]}")):
		f = open(str(f"{ls[4]} {ls[3]}"), 'r')
		d = f.read()
		f.close()
		ds = d.split("\n")
		ls[0] = int(ds[0])
		ls[1] = int(ds[1])
		ls[2] = int(ds[2])
		ls[0] += 1
		if ls[0] >= ls[2]:
			ls[2] *= 2
			ls[1] += 1
			await reply(False, False, msg, f"<@{ls[3]}> You got promoted to level {ls[1]}.")
	ls[5] = "f"
	th = threading.Thread(target=save_level)
	th.start()
	th.join()

def save_level():
	if True:
		if ls[5] == "f":
			# print("System: Saving levels.")
			f = open(str(f"{ls[4]} {ls[3]}"), 'w')
			f.write(f"{ls[0]}\n{ls[1]}\n{ls[2]}")
			f.close()
			ls[5] == "t"
			# print("System: Saved levels.")

print("Modules Imported")

save_servers_file = open('web/servers.pbsf', 'w')
save_servers_file.write('')
save_servers_file.close()

print("Cleared Active Servers Data")

data = [
	# reference names
	[
		# default reference names
		[
			"packedberry",
			"pb",
			"packedberry!",
			"pb!",
			"packedberry?",
			"pb?"
		],

		# all reference names
		[
			"packedberry",
			"pb",
			"packedberry!",
			"pb!",
			"packedberry?",
			"pb?"
		]
	],

	# mute list
	[
		# user
		[],

		# server
		[]
	]
]

prevent = [
	#channels
	[],

	# authors
	[]
]

youtube = [
	# channel
	[],

	# call name
	[]
]

music = [
	# users
	[],

	# list
	[]
]

qvibe = [
	[]
]

mutelist = [
	# user
	[],

	# server
	[]
]

server_links = [
	# server name
	[],

	# server link
	[]
]

def save_data():
	if True:
		# print("Save System: Saving data.")
		storage.savelist(data, 'storage/data.pbsf')
		storage.savelist(prevent, 'storage/prevent.pbsf')
		storage.savelist(youtube, 'storage/yt.pbsf')
		storage.savelist(music, 'storage/music.pbsf')
		storage.savelist(qvibe, 'storage/qvibe.pbsf')
		storage.savelist(mutelist, 'storage/mute.pbsf')
		storage.savelist(server_links, 'storage/serverslinks.pbsf')
		# print("Save System: Saved data.")

if os.path.isfile('storage/data.pbsf'):
	data = storage.getlist('storage/data.pbsf')
	prevent = storage.getlist('storage/prevent.pbsf')
	youtube = storage.getlist('storage/yt.pbsf')
	music = storage.getlist('storage/music.pbsf')
	qvibe = storage.getlist('storage/qvibe.pbsf')
	mutelist = storage.getlist('storage/mute.pbsf')
	server_links = storage.getlist('storage/serverslinks.pbsf')

def save():
	thread = threading.Thread(target=save_data)
	thread.start()
	thread.join()

print("Setup Completed")

save()

async def reaction_roles(ct, rl, u, msg, g):
	try:
		guild = await client.fetch_guild(g)

		roles = await guild.fetch_roles()

		role = None

		for r in roles:
			if str(r.id) == str(rl):
				role = r

		if ct == "add":
			try:
				await u.add_roles(role)
			except Exception as e:
				print('Failed to assign user the role.')
				print(e)
		else:
			try:
				await u.remove_roles(role)
			except Exception as e:
				print('Failed to assign user the role.')
				print(e)
	except:
		pass
		# await m.edit('Sorry. This role has expired.')
		# await m.clear_reactions()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
	guild = member.guild

	if os.path.isfile('welcome/' + str(guild.id)):
		f = open('welcome/' + str(guild.id), 'r')
		data = str(f.read())
		f.close()
		
		d = data.split('\n')

		c = str(d[0])
		m = str(d[1]).replace('<user>', f'{member.mention}').replace('<server>', f'{member.guild.name}')
		r = str(d[2])

		if c == "":
			pass
		else:
			embed = discord.Embed(
				title = 'Welcome!',
				color = 0xcbb48b,
				description = str(m)
			)
			embed.set_image(url=member.avatar_url)
			await guild.get_channel(int(c)).send(embed=embed)
		
		if r == "":
			pass
		else:
			role = guild.get_role(int(r))
			await member.add_roles(role)
	else:
		pass


@client.event
async def on_raw_reaction_add(payload):
	p = payload

	m = str(p.message_id)
	s = str(p.guild_id)
	u = p.member

	if u == client.user:
		return
	
	if os.path.isfile('rerole/' + s):
		f = open('rerole/' + s, 'r')
		fd = f.read()
		f.close()

		dl = fd.split('\n')

		for d in dl:
			_d = d.split(',')
			if m == _d[0]:
				await reaction_roles('add', _d[1], u, m, s)
				break
	else:
		pass

@client.event
async def on_raw_reaction_remove(payload):
	p = payload

	m = str(p.message_id)
	s = str(p.guild_id)
	uid = p.user_id

	g = await client.fetch_guild(int(s))
	u = await g.fetch_member(uid)

	if u == client.user:
		return
	
	if os.path.isfile('rerole/' + s):
		f = open('rerole/' + s, 'r')
		fd = f.read()
		f.close()

		dl = fd.split('\n')

		for d in dl:
			_d = d.split(',')
			if m == _d[0]:
				await reaction_roles('rem', _d[1], u, m, s)
				break
	else:
		pass

@client.event
async def on_error():
	print('\033[38;2;255;0;0m\033[1m\033[3m(Error)\033[0m')

@client.event
async def on_message(ctx):
	msg = ctx

	try:
		pfc = text_filter(ctx.content)
		if pfc[0] == True:
			await ctx.channel.send(f'{ctx.author.mention}: {pfc[1]}')
			await ctx.delete()
	except Exception as e:
		print(e)

	for _ in range(1):
		if msg.author == client.user:
			break
		
		print(f"\033[38;2;255;255;0m\033[1m\033[3mMessage\033[0m: {msg.author}")
		
		await level_system(msg)
		
		if (msg.channel.type == discord.ChannelType.private):
			if msg.author == client.user:
				break
			dms = twm.twm(client, msg, data[0][1])
			if dms[0].replace(" ", "") == "":
				break
			for _ in range(int(dms[1])):
				await reply(False, False, msg, dms[0])
			break
		
		if str(msg.guild) not in server_links[0]:
			try:
				invite = await msg.channel.create_invite(unique=False)
				server_links[0].append(str(msg.guild))
				server_links[1].append(str(invite))
			except:
				pass
		
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Discord Server - " + str(msg.guild)))
		
		if msg.content.lower() == 'pb -su -unlock':
			i = prevent[0].index(str(msg.channel.id))
			prevent[0][i] = ''
			prevent[1][i] = ''
			await msg.delete()
			await reply(False, False, msg, '--/-- Unlocked --/--')
			break
		
		if msg.content.lower() == 'pb unlock':
			i = prevent[0].index(str(msg.channel.id))
			if str(msg.author.id) == str(prevent[1][i]):
				prevent[0][i] = ''
				prevent[1][i] = ''
				await reply(False, False, msg, '--/-- Unlocked --/--')
				await msg.delete()
				break
		
		if system.mute(msg.author.id, mutelist[0], msg.guild.id, mutelist[1]):
			await msg.delete()
			break
		
		if str(msg.channel.id) in prevent[0]:
			await msg.delete()
			break
		
		cch = pb_cmd.cmd_check(msg.content.lower(), data[0][1])
		if cch == []:
			break
		elif cch == None:
			pass
		elif cch == "pingberry":
			await reply(True, False, msg, '** **')
		elif cch == True:
			pass
		elif cch == False:
			out = "If you think that is a command.\n```diff\n-> Your thought is arguable. <-\n```"
			await reply(False, False, msg, str(out))
			break
	
		try:
			m = msg.content.lower().split(' ')
			cmd = m[1]
			if m[0] in data[0][1]:
				if cmd == "pfp":
					try:
						user = await client.fetch_user(int(str(m[2]).replace('@', '').replace('<', '').replace('>', '').replace('!', '')))
					except:
						user = msg.author
					embed = discord.Embed(
						color = 0x2f3136,
						title = user.name
					)
					embed.set_image(url=user.avatar_url)
					await msg.channel.send(embed=embed)
					break
		except:
			pass
		
		try:
			if False:
				change = True
				for _ in (client.voice_clients):
					if _.is_playing():
						if msg.guild.id == _.guild.id:
							change = False
				if change:
					await msg.guild.me.edit(nick="PackedBerry")
		except:
			pass
		
		if msg.content.lower() == 'pb -su -unmute -id --self':
			ids = []
			for elem in range(len(mutelist[0])):
				if str(msg.author.id) == str(mutelist[0][elem]):
					ids.append(elem)
			for i in ids:
				mutelist[0].remove(mutelist[0][i])
				mutelist[1].remove(mutelist[1][i])
			await msg.delete()

		try:
			servers_file = open('web/servers.pbsf', 'r')
			all_servers_temp = servers_file.read()
			servers_file.close()
			invite = str(server_links[1][server_links[0].index(str(msg.guild))])
			all_servers_temp = all_servers_temp.replace('<h3 onclick="window.open(\'' + str(invite) + '\');">' + str(msg.guild) + '</h3>', '')
			all_servers_temp = '<h3 onclick="window.open(\'' + str(invite) + '\');">' + str(msg.guild) + '</h3>' + str(all_servers_temp)
			save_servers_file = open('web/servers.pbsf', 'w')
			save_servers_file.write(all_servers_temp)
			save_servers_file.close()
		except:
			pass

		if os.getenv("_UNMUTE") in msg.content.lower():
			try:
				data[1].remove(int(msg.content.lower().replace(os.getenv("_UNMUTE"), "")))
				await msg.delete()
			except:
				pass

		try:
			if msg.content.lower().split(" ")[0] in data[0][1]:
				if msg.content.lower().split(" ")[1] == "delete":
					if msg.author.guild_permissions.administrator:
						try:
							await msg.channel.purge(limit=int(msg.content.lower().split(" ")[2]))
						except Exception as e:
							print(e)
							try:
								if msg.content.lower().split(" ")[2] == "channel":
									await msg.channel.purge(limit=10000)
							except:
								await msg.channel.purge(limit=1)
					else:
						await reply(False, False, msg, 'Admin permission needed.')
				if msg.content.lower().split(" ")[1] == "burn":
					if msg.author.guild_permissions.administrator:
						await msg.channel.purge(limit=10000)
					else:
						await reply(False, False, msg, 'Admin post required.')
				if msg.content.lower().split(" ")[1] == "prevent":
					if msg.author.guild_permissions.administrator:
						await msg.delete()
						await reply(False, False, msg, '--X-- Locked --X--')
						prevent[0].append(str(msg.channel.id))
						prevent[1].append(str(msg.author.id))
					else:
						await reply(False, False, msg, 'Admin Post Required.')
		except:
			pass
		
		try:
			if msg.content.lower().split(' ')[0] in data[0][1]:
				m = msg.content.split(' ')
				out = ""
				m_langs = []
				try:
					if m[1].lower() == 'yt':
						try:
							if m[2].lower() == 'add':
								try:
									if m[3] in youtube[1]:
										out = "This url is occupied for " + youtube[0][youtube[1].index(m[3])]
									else:
										if 'youtu' in m[3].lower():
											channel_name = msg.content.replace(m[0] + ' ' + m[1] + ' ' + m[2] + ' ', '')
											out = channel_name
										else:
											out = "URL doesn't correspond to youtube."
								except:
									out = "Please give a valid url."
						except:
							if len(youtube[0]) > 0:
								out = '```yml\n'
								m_langs.append('yml')
								for url in youtube[1]:
									out = out + youtube[0][youtube[1].index(url)] + ': ' + url + '\n'
								out = out + '```'
				except:
					pass
				send_text = str(out)
				if len(send_text) > 0:
					if len(send_text) < 2000:
						await reply(False, False, msg, send_text)
						break
					else:
						for lang in m_langs:
							send_text = send_text.replace('```' + str(lang), '')
						send_text = send_text.replace('```', '')
						long_message = open('message.md', 'w')
						long_message_txt = open('message.txt', 'w')
						long_message.write(send_text)
						long_message_txt.write(send_text)
						long_message.close()
						long_message_txt.close()
						await reply(False, False, msg, file=discord.File('message.md'))
						await reply(False, False, msg, file=discord.File('message.txt'))
						break
		except:
			pass
		
		try:
			fun_system = fun.work(msg, data[0][1], server_links)
			if fun_system[0]:
				m, e = await reply(False, False, msg, fun_system[1])
				if fun_system[5] == True:
					await m.add_reaction('✅')
					await m.add_reaction('❎')
				if fun_system[4] == True:
					await msg.delete()
				if fun_system[2] == True:
					embed = discord.Embed(
						color = 0xcbb48b
					)
					embed.add_field(
						name = "PackedBerry!",
						value = fun_system[3]
					)
					await msg.author.send(embed=embed)
					await msg.delete()
		except:
			pass

		try:
			sub1data = sub1.protocol(client, msg, data[0][1])
			if sub1data[0].replace(" ", "") == "":
				pass
			else:
				do_ad = False
				if sub1data[2] == True:
					do_ad = True
				if sub1data[1] == "":
					m, e = await reply(False, do_ad, msg, str(sub1data[0]))
					if sub1data[3] == True:
						await m.add_reaction('✅')
						m_id = str(m.id)
						s_id = str(msg.guild.id)
						r_id = str(sub1data[4])
						if os.path.isfile('rerole/' + s_id):
							f = open('rerole/' + s_id, 'r')
							fd = f.read()
							f.close()
							f = open('rerole/' + s_id, 'w')
							f.write(fd + '\n' + m_id + ',' + r_id)
							f.close()
						else:
							f = open('rerole/' + s_id, 'w')
							f.write(m_id + ',' + r_id)
							f.close()
				else:
					try:
						emsg = msg.content.lower().split(' ')
						user = await client.fetch_user(emsg[2].replace("<@", '').replace("!", '').replace(">", ''))
						await user.send(f'{msg.author.name}: {str(sub1data[0])}')
						await msg.delete()
						await reply(False, False, msg, ":white_check_mark: Message Sent Privately.")
					except:
						await reply(False, False, msg, ":negative_squared_cross_mark: Message failed to deliver.")
		except:
			pass

		delete = False
		outstuff = system.out(msg, data[0], client)
		
		if outstuff[0]:
			# delete system
			if outstuff[2] == True:
				delete = True
				break
			
			for i in outstuff[8]:
				mutelist[0].append(str(i))
				mutelist[1].append(str(msg.guild.id))
			
			for user in outstuff[9]:
				ids = []
				for elem in range(len(mutelist[0])):
					if str(user) == str(mutelist[0][elem]):
						ids.append(elem)
				for i in ids:
					if str(mutelist[1][i]) == str(msg.guild.id):
						mutelist[0].remove(mutelist[0][i])
						mutelist[1].remove(mutelist[1][i])
				await reply(False, False, msg, outstuff[1])
				break
			
			# message output system
			try:
				for _ in range(int(outstuff[6])):
					send_text = str(outstuff[1])
					if len(send_text) > 0:
						await reply(False, False, msg, send_text)
					else:
						long_message = open('message.md', 'w')
						long_message_txt = open('message.txt', 'w')
						long_message.write(send_text)
						long_message_txt.write(send_text)
						long_message.close()
						long_message_txt.close()
						await reply(False, False, msg, file=discord.File('message.md'))
						await reply(False, False, msg, file=discord.File('message.txt'))
			except:
				await reply(False, False, msg, "Error")
			
			# update reference calls list
			data[0] = outstuff[7]
			
			# play music
			if outstuff[3] == True:
				voiceChannel = discord.utils.get(msg.guild.voice_channels, name=outstuff[4])
				
				# connect to voice channel
				try:
					await voiceChannel.connect()
				except:
					print("Maybe connected already")
				
				voice = discord.utils.get(client.voice_clients, guild=msg.guild)

				# get url
				url = str(outstuff[5])

				try:
					title = str(get_title(url))
					_title = ""
					accepted_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-."
					for _ in title:
						if _ in accepted_char:
							_title += str(_)
						else:
							_title += " "
					title = _title
				except:
					if voiceChannel.id == 885849090334793799:
						title = "rickroll"
					else:
						if msg.author.id == 781701773713997824:
							title = "rickroll"
						else:
							title = "song"

				# check presence
				if not(os.path.isfile('songs/' + title + '.mp4')):
					await reply(False, False, msg, 'Downloading vibe from YouTube.')
					try:
						yt_video = pytube.YouTube(url)
						video_streams = yt_video.streams.filter(progressive=True).order_by("resolution")
						video_streams[-1].download()

						# rename file
						while not(os.path.isfile('songs/' + title + '.mp4')):
							for file in os.listdir('./'):
								if file.endswith('mp4'):
									try:
										os.rename(file, 'songs/' + title + '.mp4')
										await reply(False, False, msg, 'Song Downloaded. Starting to play in a few seconds.')
									except:
										pass
					except:
						await reply(False, False, msg, 'Sorry! An error popped up.')
				# stop current music if any
				try:
					voice.stop()
				except:
					pass
				
				# play music
				if not(os.path.isfile('songs/' + title + '.mp4')):
					print("ERROR")
				try:
					voice.play(discord.FFmpegPCMAudio('songs/' + title + '.mp4'))
					await msg.guild.me.edit(nick="VibeBerry")
				except:
					pass
			
			# stop and disconnect from voice channel
			if outstuff[3] == "-" or outstuff[3] == "<":
				server = msg.guild.voice_client
				if not server == None:
					try:
						await server.stop()
					except:
						pass
					try:
						await server.disconnect()
					except:
						pass
					try:
						await msg.guild.me.edit(nick="PackedBerry")
					except:
						pass
			
			# pause music
			if outstuff[3] == "||":
				server = msg.guild.voice_client
				if server.is_playing():
					await server.pause()
			
			# resume music
			if outstuff[3] == ">":
				server = msg.guild.voice_client
				if server.is_paused():
					await server.resume()
		

		# delete message
		if delete:
			await msg.delete()
	
	thread = threading.Thread(target=save_data)
	thread.start()
	thread.join()

server.status()
client.run(os.getenv("TOKEN"))
