# PackedBerry

print("System Started")

import os
import discord
import server
import system
import storage
import nacl
import youtube_dl
import requests
import fun

def get_title(url: str):
	html = requests.get(url).text
	title_separator = html.split("<title>")
	title = title_separator[1].split("</title>")[0]
	return title

print("Modules Imported")

save_servers_file = open('web/servers.pbsf', 'w')
save_servers_file.write('')
save_servers_file.close()

print("Cleared Active Servers Data")

client = discord.Client()

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

def save():
	storage.savelist(data, 'storage/data.pbsf')
	storage.savelist(prevent, 'storage/prevent.pbsf')
	storage.savelist(youtube, 'storage/yt.pbsf')
	storage.savelist(music, 'storage/music.pbsf')
	storage.savelist(qvibe, 'storage/qvibe.pbsf')
	storage.savelist(mutelist, 'storage/mute.pbsf')
	storage.savelist(server_links, 'storage/serverslinks.pbsf')

if os.path.isfile('storage/data.pbsf'):
	data = storage.getlist('storage/data.pbsf')
	prevent = storage.getlist('storage/prevent.pbsf')
	youtube = storage.getlist('storage/yt.pbsf')
	music = storage.getlist('storage/music.pbsf')
	qvibe = storage.getlist('storage/qvibe.pbsf')
	mutelist = storage.getlist('storage/mute.pbsf')
	server_links = storage.getlist('storage/serverslinks.pbsf')

print("Setup Completed")

@client.event
async def on_message(msg):
	if str(msg.guild) not in server_links[0]:
		invite = await msg.channel.create_invite(unique=False)
		server_links[0].append(str(msg.guild))
		server_links[1].append(str(invite))
	
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Discord Server - " + str(msg.guild)))
	try:
		voice = discord.utils.get(client.voice_clients, guild=msg.guild)
		if voice == None or not(voice.is_playing()):
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

	if msg.author == client.user:
		save()
		return

	if os.getenv("_UNMUTE") in msg.content.lower():
		try:
			data[1].remove(int(msg.content.lower().replace(os.getenv("_UNMUTE"), "")))
			await msg.delete()
		except:
			pass

	if msg.content.lower() == 'pb -su -unlock':
		i = prevent[0].index(str(msg.channel.id))
		prevent[0][i] = ''
		prevent[1][i] = ''
		await msg.delete()
		await msg.channel.send('--/-- Unlocked --/--')
		save()
		return
	
	if msg.content.lower() == 'pb unlock':
		i = prevent[0].index(str(msg.channel.id))
		if str(msg.author.id) == str(prevent[1][i]):
			prevent[0][i] = ''
			prevent[1][i] = ''
			await msg.channel.send('--/-- Unlocked --/--')
			await msg.delete()
			save()
			return
	
	if system.mute(msg.author.id, mutelist[0], msg.guild.id, mutelist[1]):
		await msg.delete()
		save()
		return
	
	if str(msg.channel.id) in prevent[0]:
		await msg.delete()

	try:
		if msg.content.lower().split(" ")[1] == "delete":
			try:
				await msg.channel.purge(limit=int(msg.content.lower().split(" ")[2]))
			except:
				try:
					if msg.content.lower().split(" ")[2] == "channel":
						await msg.channel.purge(limit=10000)
				except:
					await msg.channel.purge(limit=1)
		if msg.content.lower().split(" ")[1] == "burn":
			await msg.channel.purge(limit=10000)
		if msg.content.lower().split(" ")[1] == "prevent":
			await msg.delete()
			await msg.channel.send('--X-- Locked --X--')
			prevent[0].append(str(msg.channel.id))
			prevent[1].append(str(msg.author.id))
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
					await msg.channel.send(send_text)
					save()
					return
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
					await msg.channel.send(file=discord.File('message.md'))
					await msg.channel.send(file=discord.File('message.txt'))
					save()
					return
	except:
		pass
	
	try:
		fun_system = fun.work(msg, data[0][1], server_links)
		if fun_system[0]:
			await msg.channel.send(fun_system[1])
			if fun_system[2] == True:
				await msg.author.send(fun_system[3])
			if fun_system[4] == True:
				await msg.delete()
	except:
		pass

	delete = False
	outstuff = system.out(msg, data[0], client)
	
	if outstuff[0]:
		# delete system
		if outstuff[2] == True:
			delete = True
			save()
			return
		
		for i in outstuff[8]:
			mutelist[0].append(str(i))
			mutelist[1].append(msg.guild.id)
		
		for user in outstuff[9]:
			for u in mutelist[0]:
				if str(user) == str(u):
					if str(msg.guild.id) == str(mutelist[1][mutelist[0].index(u)]):
						mutelist[0][mutelist[0].index(u)] = ''
						mutelist[1][mutelist[0].index(u)] = ''
						await msg.channel.send(outstuff[0])
						return
		
		# message output system
		try:
			for _ in range(int(outstuff[6])):
				send_text = str(outstuff[1])
				if len(send_text) < 2000:
					await msg.channel.send(send_text)
				else:
					long_message = open('message.md', 'w')
					long_message_txt = open('message.txt', 'w')
					long_message.write(send_text)
					long_message_txt.write(send_text)
					long_message.close()
					long_message_txt.close()
					await msg.channel.send(file=discord.File('message.md'))
					await msg.channel.send(file=discord.File('message.txt'))
		except:
			await msg.channel.send("Error")
		
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
			
			# download preferences
			ydl_opts = {
				'format': 'bestaudio/best',
				'postprocessors': [{
					'key': 'FFmpegExtractAudio',
					'preferredcodec': 'mp3',
					'preferredquality': '192',
				}],
			}
						
			# download
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				# get url
				url = str(outstuff[5])

				# get title
				try:
					title = get_title(url)
				except:
					title = "songs/song"
				
				# save file
				if not(os.path.isfile('songs/' + title + '.mp3')):
					ydl.download([url])

					# rename file
					while not(os.path.isfile('songs/' + title + '.mp3')):
						for file in os.listdir('./'):
							if file.endswith('mp3'):
								os.rename(file,'songs/' + title + '.mp3')
			
			# stop current music if any
			try:
				voice.stop()
			except:
				pass
			
			# play music
			try:
				voice.play(discord.FFmpegPCMAudio("songs/" + title + ".mp3"))
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
	
	storage.savelist(data, 'storage/data.pbsf')
	storage.savelist(prevent, 'storage/prevent.pbsf')
	storage.savelist(youtube, 'storage/yt.pbsf')
	storage.savelist(music, 'storage/music.pbsf')
	storage.savelist(qvibe, 'storage/qvibe.pbsf')
	storage.savelist(mutelist, 'storage/mute.pbsf')
	storage.savelist(server_links, 'storage/serverslinks.pbsf')

server.status()
client.run(os.getenv("TOKEN"))
