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
	dm_user = ''

	delete_me = False

	onbeta = beta.check(str(message.guild))

	try:
		if msg[0] in calls:
			try:
				if msg[1] == 'beta':
					try:
						if msg[2] == 'disable':
							if beta.check(str(message.guild)):
								beta.leave(str(message.guild))
								out = 'Server removed from beta.'
							else:
								out = 'Server is not registered in beta.'
						elif msg[2] == 'enable':
							if beta.check(str(message.guild)):
								out = 'Server already registered for beta.'
							else:
								beta.enter(str(message.guild))
								out = 'Server is now added to beta program.'
					except:
						if beta.check(str(message.guild)):
							next_file = open('data/next')
							next_data = next_file.read()
							next_file.close()
							out = str(next_data)
						else:
							out = 'Server not registered for beta. Type `pb beta enable` to register.'
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
				elif msg[1] == 'randnum':
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
				elif msg[1] == 'dm':
					dm_text = message.content.replace(_msg[0] + ' ' + _msg[1], '')
					if len(dm_text.replace(' ', '')) == 0:
						out = str(':x:')
					else:
						dm_text = message.content.replace(_msg[0] + ' ' + _msg[1] + ' ', '')
						dm = dm_text
						out = str(':white_check_mark:')
				elif onbeta and ( msg[1] == 'translate_link' or msg[1] == 'tl' ):
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
				elif onbeta and msg[1] == 'rally':
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
				elif onbeta and msg[1] == 'unrally':
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
							else:
								out = 'Never voted in the rally!'
						else:
							out = 'Rally doesn\'t exist.'
			except:
				pass
	except:
		pass

	return_test = not( out.replace(' ', '') == '' )
	do_dm_user = not( dm.replace(' ', '') == '' )

	return [
		return_test,
		out,
		do_dm_user,
		dm,
		delete_me
	]
