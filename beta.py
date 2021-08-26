# PackedBerry Beta

def check(server):
	server_files = open('beta/servers.lsv', 'r')
	servers = server_files.read().split('\n')
	server_files.close()
	if server in servers:
		return True
	else:
		return False

def leave(server):
	server_files = open('beta/servers.lsv', 'r')
	servers = server_files.read()
	server_files.close()
	beta_edit_file = open('beta/servers.lsv', 'w')
	beta_edit_file.write(servers.replace(str(server) + '\n', ''))
	beta_edit_file.close()

def enter(server):
	server_files = open('beta/servers.lsv', 'r')
	servers = server_files.read()
	server_files.close()
	beta_edit_file = open('beta/servers.lsv', 'w')
	beta_edit_file.write(str(servers) + str(server) + '\n')
	beta_edit_file.close()
