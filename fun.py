# PackedBerry Fun

import beta
import random
import translator
import os

def whitespace(val):
	if len(str(val).replace(' ', '')) == 0:
		return True
	else:
		return False

def work(message, calls, server_links):
	msg = message.content.lower().split(' ')
	_msg = message.content.split(' ')

	out = ''
	dm = ''
	polling = False

	no_reply = True

	delete_me = False

	human = False

	captcha_file = open('fun/captcha/human_verified', 'r')
	captcha_data = captcha_file.read()
	captcha_file.close()

	human_table = captcha_data.split('\n')

	for id in human_table:
		if str(id) == str(message.author.id):
			human = True
			break

	onbeta = beta.check(str(message.guild))

	try:
		if msg[0] in calls:
			try:
				if msg[1] in ['in-dev', 'indev']:
					try:
						if msg[2] == 'disable':
							if beta.check(str(message.guild)):
								beta.leave(str(message.guild))
								out = 'Server removed from in-dev.'
							else:
								out = 'Server is not registered in in-dev.'
						elif msg[2] == 'enable':
							if beta.check(str(message.guild)):
								out = 'Server already registered for in-dev.'
							else:
								beta.enter(str(message.guild))
								out = 'Server is now added to in-dev commands.'
					except:
						if beta.check(str(message.guild)):
							next_file = open('data/next')
							next_data = next_file.read()
							next_file.close()
							out = str(next_data)
						else:
							out = 'Server not registered for in-dev commands. Type `pb in-dev enable` to register.\n\n```It is not recommended to use in-dev commands. They have incomplete code and may not function as expected. These may also have a chance of crashing bot and doing some problematic stuff to server.```'
				elif msg[1] == 'human':
					if human:
						out = 'You are verified as human.'
					else:
						out = 'You are not verified as human. Type `<prefix> captcha` to start the process.'
				elif msg[1] == 'invite':
					try:
						if msg[2] in msg:
							if str(message.content.replace(msg[0] + ' ' + msg[1] + ' ', '')).replace(' ', '') != '':
								if message.content.replace(msg[0] + ' ' + msg[1] + ' ', '') in server_links[0]:
									invite = str(server_links[1][server_links[0].index(str(message.content.replace(msg[0] + ' ' + msg[1] + ' ', '')))])
									out = str(invite)
								else:
									out = 'Invalid Server Name'
							else:
								invite = str(server_links[1][server_links[0].index(str(message.guild))])
								out = str(invite)
					except:
						invite = str(server_links[1][server_links[0].index(str(message.guild))])
						out = str(invite)
				elif msg[1] == 'random-number':
					try:
						try:
							out = str(random.randint(int(msg[2]), int(msg[3])))
						except:
							out = str(random.randint(0, int(msg[2])))
					except:
						out = str(random.randint(0, 1000000000))
				elif msg[1] == 'choose':
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
				elif msg[1] == 'dm-me':
					dm_text = message.content.replace(_msg[0] + ' ' + _msg[1], '')
					if len(dm_text.replace(' ', '')) == 0:
						out = str(':x: Please provide some text to message you.')
					else:
						dm_text = message.content.replace(_msg[0] + ' ' + _msg[1] + ' ', '')
						dm = dm_text
						out = str(':white_check_mark: Sent message to you privately.')
				elif ( msg[1] == 'translate' or msg[1] == 'tr' ):
					try:
						if whitespace(msg[2]):
							out = 'Missing value for destination/to language.'
						else:
							try:
								if whitespace(msg[3]):
									out = 'Need something to translate.'
								else:
									translation_text = message.content.replace(f"{_msg[0]} {_msg[1]} {_msg[2]} ", '')
									dest_lang = str(msg[2])
									translation = translator.translate(translation_text, dest_lang)
									original_message = message.content.replace(_msg[0] + ' ' + _msg[1] + ' ' + _msg[2] + ' ', '')
									out = '<@' + str(message.author.id) + '>\'s Original Message: ' + original_message + '\n<@' + str(message.author.id) + '>\'s Translated Message: ' + str(translation)
									delete_me = True
							except:
								out = 'Need something to translate.'
					except:
						out = 'Missing value for destination/to language.'
				elif ( msg[1] == 'translate_link' or msg[1] == 'tl' ):
					try:
						if whitespace(msg[2]):
							out = 'Missing value for destination/to language.'
						else:
							try:
								if whitespace(msg[3]):
									out = 'Need something to translate.'
								else:
									translation_text = message.content.replace(f"{_msg[0]} {_msg[1]} {_msg[2]} ", '')
									dest_lang = str(msg[2])
									translation = translator.backup_translate(translation_text, dest_lang)
									original_message = message.content.replace(_msg[0] + ' ' + _msg[1] + ' ' + _msg[2] + ' ', '')
									out = '<@' + str(message.author.id) + '>\'s Original Message: ' + original_message + '\n<@' + str(message.author.id) + '>\'s Translated Message: ' + str(translation)
									delete_me = True
							except:
								out = 'Need something to translate.'
					except:
						out = 'Missing value for destination/to language.'
				elif msg[1] == 'rally':
					if len(msg) < 3:
						out = 'Need some rally name to start or vote.'
					else:
						rally_name = str(message.content.lower().replace(msg[0] + ' ' + msg[1] + ' ', ''))
						if os.path.isfile('rally/' + rally_name):
							rally_file_read = open('rally/' + str(rally_name), 'r')
							rally_file_read_data = rally_file_read.read()
							rally_file_read.close()
							if str(message.author.id) in rally_file_read_data:
								out = 'Already voted for rally!'
							else:
								rally_file_write = open('rally/' + str(rally_name), 'w')
								rally_file_write.write(rally_file_read_data + '\n' + str(message.author.id))
								rally_file_write.close()
								if rally_file_read_data.replace('\n', '') == '':
									out = 'Created and voted.'
								else:
									out = 'Voted.'
						else:
							rally_file_write = open('rally/' + str(rally_name), 'w')
							rally_file_write.write('\n' + str(message.author.id))
							rally_file_write.close()
							out = 'Created and voted.'
				elif msg[1] == 'unrally':
					if len(msg) < 3:
						out = 'Need some rally name to remove vote.'
					else:
						rally_name = message.content.lower().replace(msg[0] + ' ' + msg[1] + ' ', '')
						if os.path.isfile('rally/' + rally_name):
							rally_file_read = open('rally/' + str(rally_name), 'r')
							rally_file_read_data = rally_file_read.read()
							rally_file_read.close()
							if str(message.author.id) in rally_file_read_data:
								rally_file_write = open('rally/' + str(rally_name), 'w')
								rally_file_write.write(str(rally_file_read_data.replace(str(message.author.id), '')))
								rally_file_write.close()
								out = 'Removed vote for rally!'
								votes = 0
								vote_count_list = str(rally_file_read_data.replace(str(message.author.id), '')).split('\n')
								for v in vote_count_list:
									if v == '':
										pass
									else:
										votes = votes + 1
								if votes == 0:
									os.remove('rally/' + str(rally_name))
							else:
								out = 'Never voted in the rally!'
						else:
							out = 'Rally doesn\'t exist.'
				elif msg[1] == 'rally-count':
					if len(msg) < 3:
						out = 'Need some rally name to count votes.'
					else:
						rally_name = message.content.lower().replace(msg[0] + ' ' + msg[1] + ' ', '')
						if os.path.isfile('rally/' + rally_name):
							rally_file_read = open('rally/' + str(rally_name), 'r')
							rally_file_read_data = rally_file_read.read()
							rally_file_read.close()
							votes_list = rally_file_read_data.split('\n')
							votes = 0
							for v in votes_list:
								if v == '':
									pass
								else:
									votes = votes + 1
							out = str(votes) + ' votes.'
						else:
							out = '0 Votes(Maybe Rally Doesn\'t exists or you might have mispelled).'
				elif msg[1] == 'license':
					out = "```md\n"
					license_file = open('legal/Licenses/ASBL.md', 'r')
					license = license_file.read()
					license_file.close()
					out = out + str(license) + '\n```'
				elif msg[1] == 'credits':
					out = """
Credits for making `PackedBerry` a thing!
```yml
Attachment Aditya: Creator
Attachment Studios: Production Partners
Python 3.8: Project Base Services
Discord: API And Usage Services
ReplIt: Editing And Hosting Services
UptimeRobot: Monitoring And Hosting System
GitHub: Storage Services
```
Licensed under `ASBL 3.0`
"""
				elif ( msg[1] == 'captcha' ):
					captcha_text = ''
					chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[]\\;\',./~!@#$%^&()+{}|:"<>?'
					for _ in range(6):
						captcha_text += str(chars[random.randint(0, len(chars) - 1)])
					dm = 'You captcha code is `' + captcha_text.replace('`', '\\`') + '`.'
					user_captcha_file = open('fun/captcha/' + str(message.author.id), 'w')
					user_captcha_file.write(captcha_text)
					user_captcha_file.close()
					out = 'Type `<prefix> verify <captcha>` in the server to verify captcha.'
				elif ( msg[1] == 'verify' ):
					try:
						if whitespace(msg[2]):
							out = 'Expected some value to clear captcha. Type `<prefix> captcha` to get a dm with captcha.'
						else:
							if os.path.isfile('fun/captcha/' + str(message.author.id)):
								user_captcha_file = open('fun/captcha/' + str(message.author.id), 'r')
								user_captcha_file_read = user_captcha_file.read()
								user_captcha_file.close()
								if str(_msg[2]) == str(user_captcha_file_read):
									out = 'verified'
									os.remove('fun/captcha/' + str(message.author.id))
									hvf = open('fun/captcha/human_verified', 'r')
									hvfd = str(str(hvf.read().replace(str(message.author.id), '')) + '\n' + str(message.author.id))
									hvf.close()
									hvf = open('fun/captcha/human_verified', 'w')
									hvf.write(hvfd)
									hvf.close()
								else:
									out = 'Captcha failed. Type `<prefix> captcha` to restart.'
									os.remove('fun/captcha/' + str(message.author.id))

							else:
								out = 'No captcha found. Type `<prefix> captcha` to get one.'
					except:
						out = 'Expected some value to clear captcha. Type `<prefix> captcha` to get one.'
				elif ( msg[1] == 'table_tennis' or msg[1] == 'tt' ):
					os.mkdir('fun/tt/' + str(message.author.id))
					tt_file = open('fun/tt/' + str(message.author.id) + '/score', 'w')
					tt_file.write('0')
					tt_file.close()
					tt_file = open('fun/tt/' + str(message.author.id) + '/pb', 'w')
					tt_file.write('')
					tt_file.close()
					out = """
Type `ping <speed-value> <direction-value>` to give your move.
( Note that you can use values from table only. )

Values for hit parameters:
```
+------------------------------------+
|v: speed values  | direction values |
+------------------------------------+
|a: max           | extreme left     |
|b: above average | left             |
|c: average       | middle           |
|d: below average | right            |
|e: min           | extreme right    |
+-----------------+------------------+
```
"""
				elif ( msg[1].replace('!', '') in ['hi', 'hello', 'yo'] ):
					out = 'Hello!'
				elif msg[1] == 'sus':
					out = '<@' + str(message.author.id) + '> is sus.'
				elif False and onbeta and msg[1] == 'amogus':
					dm = ['Crewmate', 'Impostor'][random.randint(0, 1)]
					au_server_file = open('fun/amogus/' + str(message.author.id), 'w')
					au_server_file.write(str(dm))
					au_server_file.close()
					dm = 'Your color is Lime. Your role is ' + str(dm) + '.'
					out = 'Your role is in DM. Type `amogus report` in the server to start.'
				elif msg[1] in ['hotcold', 'hc']:
					guess_num = random.randint(1, 20)
					try:
						guess_num = random.randint(1, int(msg[2]))
					except:
						pass
					hc_server_file = open('fun/hc/' + str(message.author.id), 'w')
					hc_server_file.write(str(guess_num))
					hc_server_file.close()
					out = 'Type `hotcold number` to give the number.'
				elif msg[1] in ['nomenclate', 'name']:
					vowels = 'aeiou'
					consonants = 'bcdfgjklmnpstv'
					char_turn_id = random.randint(0, 1)
					output_name = ''
					repeat_amount = random.randint(4, 6)
					try:
						if int(msg[2]) == 0:
							pass
						elif int(msg[2]) < 0:
							repeat_amount = int(msg[2]) * -1
						else:
							repeat_amount = int(msg[2])
					except:
						pass
					for _ in range(repeat_amount):
						if char_turn_id == 0:
							ch_id = random.randint(0, len(vowels) - 1)
							char = vowels[ch_id]
							output_name += str(char)
							char_turn_id = ( char_turn_id - 1 ) * -1
						else:
							ch_id = random.randint(0, len(consonants) - 1)
							char = consonants[ch_id]
							output_name += str(char)
							char_turn_id = ( char_turn_id - 1 ) * -1
					out = str(output_name)
				elif msg[1] in ['random-rearrangement', 'nag-a-ram']:
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
				elif msg[1] == 'servers':
					server_list = (sorted(server_links[0]))
					top_list = server_list[0:15]
					server_string = '```'
					for s in top_list:
						server_string += '\n' + str(s)
					server_string += '\n```'
					out = str(server_string)
				elif msg[1] == 'rally-list':
					rallies = os.listdir('rally')
					top_list = rallies[0:15]
					top_list = sorted(top_list)
					name_string = '```'
					for s in top_list:
						name_string += '\n' + str(s)
					name_string += '\n```'
					out = str(name_string)
				elif msg[1] == 'say':
					try:
						if whitespace(msg[2]):
							out = 'Need some text.'
						else:
							_text = ''
							for t in range(len(_msg)):
								if t == 0 or t == 1:
									pass
								else:
									if t == len(_msg) - 1:
										_text += str(_msg[t])
									else:
										_text += str(_msg[t]) + ' '
							out = _text
							delete_me = True
					except:
						out = 'Need some text to say.'
				elif msg[1] == 'poll':
					try:
						if whitespace(msg[2]):
							out = 'Need some poll text.'
						else:
							poll_text = ''
							for t in range(len(_msg)):
								if t == 0 or t == 1:
									pass
								else:
									if t == len(_msg) - 1:
										poll_text += str(_msg[t])
									else:
										poll_text += str(_msg[t]) + ' '
							out = poll_text
							polling = True
							delete_me = True
					except:
						out = 'Need some poll text.'
				else:
					no_reply = True
			except:
				pass
	except:
		pass
	
	if no_reply:
		_msg_full = message.content
		msg_full = message.content.lower()

		_msg = _msg_full.split(' ')
		msg = msg_full.split(' ')

		if msg[0] == 'ping':
			try:
				if os.path.isfile('fun/tt/' + str(message.author.id) + '/score'):
					def remove_src():
						os.remove('fun/tt/' + str(message.author.id) + '/score')
						os.remove('fun/tt/' + str(message.author.id) + '/pb')
						os.rmdir('fun/tt/' + str(message.author.id))
					score_file_read = open('fun/tt/' + str(message.author.id) + '/score', 'r')
					score = score_file_read.read()
					score_file_read.close()
					score_file_write = open('fun/tt/' + str(message.author.id) + '/score', 'w')
					pb_file_read = open('fun/tt/' + str(message.author.id) + '/pb', 'r')
					pb_data = pb_file_read.read()
					pb_file_read.close()
					pb_file_write = open('fun/tt/' + str(message.author.id) + '/pb', 'w')
					try:
						values = ['a', 'b', 'c', 'd', 'e']
						if msg[1] in values:
							speed = values.index(msg[1])
							try:
								if msg[2] in values:
									direction = values.index(msg[2])
									pb_speed = 0
									pb_dir = 0
									if pb_data == '':
										pass
									else:
										pb_dir = values.index(pb_data.split(' ')[2])
										pb_speed = values.index(pb_data.split(' ')[1])
										pb_dir = pb_dir + random.randint( ( -1 * pb_speed - 2 ), ( 1 * pb_speed - 2 ) )
									pl_dir = direction + random.randint( ( -1 * speed - 2 ), ( 1 * speed - 2 ) ) + pb_dir
									if pl_dir < -2 or pl_dir > 2:
										out = 'Your accuracy failed, ball went outside the table. Your score: ' + score
									else:
										if pl_dir < 0:
											pb_dir = [ 'c', 'd', 'e' ][random.randint(0, 2)]
										elif pl_dir > 0:
											pb_dir = [ 'c', 'b', 'a' ][random.randint(0, 2)]
										else:
											pb_dir = [ 'e', 'd', 'c', 'b', 'a' ][random.randint(0, 4)]
									pb_speed = 'c'
									if out == '':
										pb_data = 'pong ' + pb_speed + ' ' + pb_dir
										out = pb_data
										score = int(score) + 1
										score = str(score)
								else:
									out = 'You messed up. Add some options to your hit. Your score: ' + score
									remove_src()
							except:
								out = 'You messed up. Have speed and direction in your hit. Your score: ' + score
								remove_src()
						else:
							out = 'You messed up. Your score: ' + score
							remove_src()
					except:
						out = 'You messed up. Your score: ' + score
						remove_src()
					score_file_write.write(score)
					score_file_write.close()
					pb_file_write.write(pb_data)
					pb_file_write.close()
			except:
				pass
	
	if message.content.lower() == 'ping':
		out = 'pong'
	if message.content.lower() == 'pong':
		out = 'ping'
	if msg[0] in calls:
		real_message = message.content.lower().replace(msg[0] + ' ', '')
		if real_message in ['shut up', 'just shut up', 'stay quiet', 'I request you to not leak secrets.']:
			out = 'Not in this life! :stuck_out_tongue_winking_eye:'
	if 'red' in message.content.lower():
		if out == '':
			out = 'sus.'
	
	"""
	try:
		if onbeta and msg[0] == 'amogus':
			try:
				if not(whitespace(msg[1])):
					if os.path.isfile('fun/amogus/' + str(message.author.id)):
						if msg[1] == 'report':
							out = ""\"
Dead Body Reported.
""\"
					else:
						out = 'No game found.'
			except:
				out = '|| a |||| m |||| o |||| g |||| u |||| s ||'
	except:
		pass
	"""
	
	try:
		if msg[0] in ['hotcold', 'hc']:
			hc_file = open('fun/hc/' + str(message.author.id), 'r')
			hc_num = int(hc_file.read())
			hc_file.close()
			try:
				if int(msg[1]) == int(hc_num):
					out = 'Correct!'
					if random.randint(1, 10) == 1:
						out = 'Goldilocks.'
					os.remove('fun/hc/' + str(message.author.id))
				elif int(msg[1]) < int(hc_num):
					out = 'Cold.'
				elif int(msg[1]) > int(hc_num):
					out = 'Hot.'
			except:
				out = 'Numeric Input Required.'
	except:
		pass

	return_test = not( out.replace(' ', '') == '' )
	do_dm_user = not( dm.replace(' ', '') == '' )

	return_stuff = [
		return_test,
		out,
		do_dm_user,
		dm,
		delete_me,
		polling
	]
	
	return return_stuff
