PackedBerry Command Details

Use prefixes before main command.
Commands are space sensitive.
Type "pb call" to get all prefixes.
Type "pb in-dev" to get all hidden in development commands(not recommended).

Items covered by '[' and ']' are optional.
Items covered by '"' and '"' are values and can not be changed.
Items covered by '<' and '>' are dependent on you to set.
Items covered by '(' and ')' are compulsory.

--------------------------------
-- System Information Commands --
help:
	syntax: <prefix> help
	usage: Get all commands.
version:
	syntax: <prefix> version
	usage: Get version of PackedBerry Service being used.
whatsnew:
	syntax: <prefix> whatsnew
	usage: Gets information about whats new in version of PackedBerry Bot.
credits:
	syntax: <prefix> credits
	usage: Returns credits for PackedBerry.
license:
	syntax: <prefix> credits
	usage: Returns main license for PackedBerry.

-- Bot Settings Commands --
call:
	syntax: <prefix> call [name]
	usage: Gets all available prefixes to use if [name] not provided. If [name] given then adds [name] to the list of available prefixes.
nocall:
	syntax: <prefix> nocall (name)
	usage: Removes (name) from the list of all available prefixes unless (name) is a system default prefix.

-- Moderation Commands --
delete:
	syntax: <prefix> delete (amount)
	usage: Deletes (amount) number of messages.
burn:
	syntax: <prefix> burn
	usage: Used to empty the channel.
prevent:
	syntax: <prefix> prevent
	usage: Locks the channel and prevents to write anything in it.
unlock:
	syntax: <prefix> unlock
	usage: Unlocks the channel if locked.
mute:
	syntax: <prefix> mute (user)
	usage: Mutes the user and doesn't let him talk.
unmute:
	syntax: <prefix> unmute (user)
	usage: Unmutes the user and so he can talk.

-- Vibes/Music Commands --
vibe:
	syntax: <prefix> vibe (url) (voice channel)
	usage: Plays music from YouTube with url as (url) in the (voice channel).
novibe:
	syntax: <prefix> novibe
	usage: Stops playing music and disconnets from voice channel.
pausevibe:
	syntax: <prefix> pausevibe
	usage: Pauses the music till it is resumed again.
resumevibe:
	syntax: <prefix> resumevibe
	usage: Resumes music if paused.
donevibe:
	syntax: <prefix> donevibe
	usage: Ends the music.

-- Multiple Servers Commands --
in-dev:
	syntax: <prefix> in-dev
	usage: Gives message about current in-dev features if enabled.
invite:
	syntax: <prefix> invite [server]
	usage: Sends invite of current server if [server] not given, else gives invite for [server].
server:
	syntax: <prefix> server [server-id]
	usage: Gets information about server with id as [server-id] where [server-id] is set default for current server.
servers:
	syntax: <prefix> servers
	usage: Sends a list of servers which contain PackedBerry bot.

-- Fun Commands --
hi:
	syntax: <prefix> hi
	usage: Sends Hello.
ping:
	syntax: <prefix> ping
	usage: Pings the user who called the command.
spam:
	syntax: <prefix> spam (amount) (text)
	usage: Spams (text) (amount) number of times. Maximum value for (amount) is 25 and minimum is 1.
sitename:
	syntax: <prefix> sitename (url)
	usage: Gets the title of site from (url)
img:
	syntax: <prefix> img [seed]
	usage: Sends a random image if no seed else with seed gives specific output.
dm-me:
	syntax: <prefix> dm-me (message)
	usage: DMs [Message] to message author privately.
dm-user:
	syntax: <prefix> dm-user (user) (message)
	usage: DMs [Message] to (user) privately.
say:
	syntax: <prefix> say (message)
	usage: Says (message) given by user in the server.
random-number:
	syntax: <prefix> random-number [lower_limit] [upper_limit]
	usage: Returns a randum number. If limits given, picks a number between [lower_limit] and [upper_limit]. If only one limit specified, assumes limit given is [upper_limit] and [lower_limit] be 0.
choose:
	syntax: <prefix> choose (option1) [option2] [option3] [option4] [option...]
	usage: Chooses one option from given options.
random-rearrangement:
	syntax: <prefix> random-rearrangement (text)
	usage: Randomly rearranges the letters of (text).
translate:
	syntax: <prefix> translate (destination-language) (text)
	usage: Translates (text) to (destination-language).
translate_link:
	syntax: <prefix> translate_link (destination-language) (text)
	usage: Translates (text) to (destination-language) and sends link for accessing translation.
table_tennis:
	syntax: <prefix> table_tennis
	usage: Starts a solo table tennis match.
ping:
	syntax: ping
	usage: Replies "pong".
rally:
	syntax: <prefix> rally (rally-name)
	usage: Creates(if not) and votes to (rally-name).
unrally:
	syntax: <prefix> unrally (rally-name)
	usage: Removes user votes from (rally-name).
rally-list:
	syntax: <prefix> rally-list
	usage: Returns list of available rallies.
rally-count:
	syntax: <prefix> rally-count (rally-name)
	usage: Counts votes for (rally-name).
captcha:
	syntax: <prefix> captcha
	usage: Sends a verification code in dm.
verify:
	syntax: <prefix> verify (code)
	usage: Verifies user if (code) matches.
human:
	syntax: <prefix> human
	usage: Says if mesage author is verified as human by PackedBerry.
sus:
	syntax: <prefix> sus
	usage: Responds user is sus.
amogus(postponed):
	syntax: <prefix> amogus
	usage: in dev, amogus game.
hotcold:
	syntax: <prefix> hotcold [limit]
	usage: Starts a game of `HotCold`. Player guesses a number. If cold the number is larger and if hot then smaller.
nomenclate:
	syntax: <prefix> nomenclate [word-size]
	usage: Creates a random word that can be okay enough for being pronounced. It [word-size] given, sends word with given [word-size].
poll:
	syntax: <prefix> poll (topic)
	usage: Creates a yes-no poll for (topic).

--------------------------------