# PackedBerry Commands

mt = [
	"img", "image", "pic", "picsum", "photo",
	"spam",
	"ping",
	"pong",
	"invite"
]

games = {
	"hc": "Hot Cold - Guess The Number",
	"hotcold": "Hot Cold - Guess The Number",
	"ping": "Table Tennis Match"
}

pb = {
	"help" : "Help",
	"ver" : "Version",
	"version" : "Version",
	"whatsnew" : "Whatsnew",
	"wn" : "Whatsnew",
	"latency" : "Delays",
	"credits" : "Credits",
	"credit" : "Credits",
	"license" : "ASBL V3",
	"call" : "Prefixes",
	"nocall" : "Prefixes",
	"delete" : "Clean Up",
	"burn" : "Clean Up",
	"prevent" : "Lock Channel",
	"unlock" : "Unlock Channel",
	"mute" : "Mute User",
	"unmute" : "Unmute User",
	"vibe" : "Play Audio From YouTube",
	"novibe" : "Exit Voice Channel",
	"pausevibe" : "Pause On Going Audio",
	"resumevibe" : "Resume On Going Audio",
	"donevibe" : "Stop On Going Audio",
	"in-dev" : "In Development List",
	"indev" : "In Development List",
	"invite" : "Server Invitation",
	"server" : "Server Information",
	"servers" : "Connected Servers",
	"hi" : "Greetings",
	"hello" : "Greetings",
	"yo" : "Greetings",
	"ping" : "Ping User",
	"spam" : "Spam",
	"sitename" : "Site Name",
	"img" : "Image",
	"pic" : "Image",
	"photo" : "Image",
	"image" : "Image",
	"picsum" : "Image",
	"dm-me" : "DM",
	"dm-user" : "DM",
	"dm" : "DM",
	"say" : "Says",
	"random-number" : "Random Number Generator",
	"choose" : "Random Selector",
	"random-rearrangement" : "Super Random Anagram",
	"translate(limited)" : "Translation",
	"tr" : "Translation",
	"translate_link" : "Translation",
	"tl" : "Translation",
	"table-tennis" : "Mini Game - Table Tennis",
	"tt" : "Mini Game - Table Tennis",
	"pong" : "PONG",
	"rally" : "Politics",
	"unrally" : "Politics",
	"rally-list" : "Politics",
	"rally-count" : "Politics",
	"captcha" : "Human Check",
	"verify" : "Human Check",
	"human" : "Human Check",
	"sus" : "Hmmmmmmmmmmmmmmmmmmmmm...",
	"amogus" : "DED",
	"hotcold" : "Mini Game - HotCold Numbers",
	"hc" : "Mini Game - HotCold Numbers",
	"nomenclate" : "Nomenclate",
	"name" : "Nomenclate",
	"poll" : "Poll",
	"coin": "Flip A Coin",
	"level": "Chat Level",
	"levels": "Chat Level",
	"xp": "Chat XP",
	"messages": "Message Count",
	"ad": "Advertisement",
	"advertisement": "Advertisement",
	"scam": "Advertisement",
	"role": "Get Role",
	"welcome": "Welcome Commands",
	"tac": "Terms and Conditions",
	"pfp": "Profile Picture",
	"quote": "Quote",
	"cross-server": "Cross Server Messages - Global Messages",
	"set-spam": "Spam Options",
	"setup": "PackedBerry Configuration",
	"update": "PackedBerry Configuration"
}

def cmd(message):
	msg = message.split(' ')
	try:
		r = msg[1]
		if r in pb:
			pass
		else:
			r = msg[0]
			if r in games:
				pass
			else:
				r = "Hmmm..."
	except:
		r = msg[0]
		if r in games:
			pass
		else:
			r = "Hmmm..."
	return r

def cmd_check(message, data_list):
	msg = message.lower().split(' ')
	if msg[0] in data_list:
		try:
			if msg[1] in pb:
				return True
			else:
				return False
		except:
			return None
	else:
		if "red" in message:
			return None
		elif "694131271776862259" in message or "781701773713997824" in message:
			return "pingberry"
		elif msg[0] in games:
			return "nope"
		else:
			return []

def emb_check(message):
	if cmd(message) in mt:
		return False
	else:
		return True

def cmd_key(message):
	msg = message.split(" ")
	if len(msg) < 2:
		try:
			if str(msg[0]).lower() in pb:
				return pb[str(msg[0]).lower()]
			else:
				return games[str(msg[0]).lower()]
		except:
			return "Hmmm..."
	else:
		try:
			if str(msg[1]).lower() in pb:
				return pb[str(msg[1]).lower()]
			else:
				return games[str(msg[0]).lower()]
		except:
			return "Hmmm..."
