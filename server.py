# PackedBerry Server

from flask import Flask
from threading import Thread
import logging

app = Flask('')

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def home():
	start_file = open("web/start.html", "r")
	start = start_file.read()
	start_file.close()
	server_file = open("web/servers.pbsf", "r")
	servers = server_file.read()
	server_file.close()
	mid_file = open("web/mid.html", "r")
	mid = mid_file.read()
	mid_file.close()
	mid_file2 = open("web/mid2.html", "r")
	mid2 = mid_file2.read()
	mid_file2.close()
	help_file = open("data/help", "r")
	help_data = help_file.read().replace('\n', '<br>').replace('\t', '<tab></tab>').replace('`', '').replace('diff', '')
	help_file.close()
	more_help_file = open('data/d_help', 'r')
	help_data = help_data + '</p><h2>Detailed Help</h2><p>' + more_help_file.read().replace('>', '&gt;').replace('<', '&lt;').replace('\n', '<br>').replace('\t', '<tab></tab>').replace('`', '').replace('diff', '')
	more_help_file.close()
	end_file = open("web/end.html", "r")
	end = end_file.read()
	end_file.close()
	html = start + servers + mid + mid2 + help_data + end
	return html

def run():
	app.run(host='0.0.0.0',port=2021)

def status():
	t = Thread(target=run)
	t.start()
