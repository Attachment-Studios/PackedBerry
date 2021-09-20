# PackedBerry Translation System

from translate import Translator as tr
from langdetect import detect

def translate(text: str, dest: str):
	fl = detect(text)
	translator = tr(from_lang=str(fl), to_lang=str(dest))
	translation = translator.translate(text)
	translation = translation.replace('&#39;', "'").replace('&#10;', "\n")
	return str(translation)

def backup_translate(text: str, dest: str):
	gt_ch_format = {
		"%": "%25",
		"\n": "%0A",
		" ": "%20",
		"`": "%60",
		"@": "%40",
		"#": "%23",
		"$": "%24",
		"^": "%5E",
		"&": "%26",
		"+": "%2B",
		"=": "%3D"
	}

	text_gt_format = text.replace('', '')
	
	for key in gt_ch_format:
		text_gt_format = text_gt_format.replace(key, gt_ch_format[key])
	
	url = f'https://translate.google.com/?sl=auto&tl={dest}&text={text_gt_format}&op=translate'
	
	translation = str(url)
	return translation
