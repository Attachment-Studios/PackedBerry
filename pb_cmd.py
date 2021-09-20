# PackedBerry Commands

mt = [
	"img", "image", "pic", "picsum", "photo",
	"spam",
	"ping",
	"pong",
	"invite"
]

pb = {
	"help" : "Help",
	"ver" : "Version",
	"version" : "Version",
	"whatsnew" : "Whatsnew",
	"wn" : "Whatsnew",
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
	"table_tennis" : "Mini Game - Table Tennis",
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
	"amogus(dev, unstable)" : "DED",
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
}

def cmd(message):
	msg = message.split(' ')
	try:
		r = msg[1]
	except:
		r = "Hmmm..."
	return r

def cmd_check(message, data_list):
	msg = message.split(' ')
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
			return pb[str(msg[0]).lower()]
		except:
			return "Hmmm..."
	else:
		try:
			return pb[str(msg[1]).lower()]
		except:
			return "Hmmm..."
