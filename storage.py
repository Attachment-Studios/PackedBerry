# PackedBerry Storage

def savelist(savelist, savename):
	save_string = ''
	if len(savelist) < 1:
		save_string += '//voidlist//'
	for elem in savelist:
		save_string += '//PBS//'
		if str(type(elem)).replace('<class \'', '').replace('\'>', '') == "list":
			if len(elem) < 1:
				save_string += '//voidlist//'
			for el in elem:
				save_string += '//PBSM//'
				if str(type(el)).replace('<class \'', '').replace('\'>', '') == "list":
					if len(el) < 1:
						save_string += '//voidlist//'
					for e in el:
						save_string += '//PBSSM//'
						save_string += str(e)
						save_string += '//PBSSM//'
				else:
					save_string += str(el)
				save_string += '//PBSM//'
		else:
			save_string += str(elem)
		save_string += '//PBS//'
	savefile = open(str(savename), 'w')
	savefile.write(save_string)
	savefile.close()

def getlist(savefile):
	try:
		savefile = open(str(savefile), 'r')
		data = savefile.read()
		savefile.close()
		list_data = data.split('//PBS//')
		for num in range(list_data.count('')):
			list_data.remove('')
		for elem in list_data:
			if elem == '//voidlist//':
				list_data[list_data.index(elem)] = []
			else:
				if '//PBSM//' in elem:
					list_data[list_data.index(elem)] = list_data[list_data.index(elem)].split('//PBSM//')
		for elem in list_data:
			if str(type(elem)).replace('<class \'', '').replace('\'>', '') == "list":
				for num in range(list_data[list_data.index(elem)].count('')):
					elem.remove('')
				for el in elem:
					if el == '//voidlist//':
						list_data[list_data.index(elem)][list_data[list_data.index(elem)].index(el)] = []
					else:
						if '//PBSSM//' in el:
							list_data[list_data.index(elem)][list_data[list_data.index(elem)].index(el)] = el.split('//PBSSM//')
		for elem in list_data:
			if str(type(elem)).replace('<class \'', '').replace('\'>', '') == "list":
				for el in elem:
					if str(type(el)).replace('<class \'', '').replace('\'>', '') == "list":
						for e in el:
							for n in range(list_data[list_data.index(elem)][list_data[list_data.index(elem)].index(el)].count('')):
								list_data[list_data.index(elem)][list_data[list_data.index(elem)].index(el)].remove('')
							if e == '//voidlist//':
								list_data[list_data.index(elem)][list_data[list_data.index(elem)].index(el)] = []
		return list_data
	except:
		pass


def saveitem(value, savefile):
	save = open(savefile, 'w')
	save.write(value)
	save.close()

def getitem(savefile):
	try:
		save = open(savefile, 'r')
		value = save.read()
		save.close()
		return value
	except:
		pass

