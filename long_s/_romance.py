import re
from unidecode import unidecode

def french_conversion(text):
	clean_text = unidecode(text)

	# selects every S that has a letter (or hyphen) after it,
	# so long as that letter is not B, F, nor H.
	pattern = r"s(?=[a-ac-eg-gi-zA-AC-EG-GI-Z])"
	indices = [m.start() for m in re.finditer(pattern, clean_text)]
	for i in indices:
		text = text[:i] + "ſ" + text[i + 1: ]

	return text


def italian_conversion(text):
	USE_DOUBLE_LONG_WITH_SSI = True

	# selects every S that has a letter (or hyphen) after it,
	# so long as that letter is not B nor F.
	clean_text = unidecode(text)
	pattern = r"s(?=[a-ac-eg-zA-AC-EG-Z-—])"
	indices = [m.start() for m in re.finditer(pattern, clean_text)]

	# excludes any S that occurs before an accented vowel.
	pattern = r"s(?=[áàéèíìóòúüÁÀÉÈÍÌÓÒÚÙÜ])"
	excluded_indices = [m.start() for m in re.finditer(pattern, text)]
	indices = [i for i in indices if i not in excluded_indices]
	for i in indices:
		text = text[:i] + "ſ" + text[i + 1: ]

	if USE_DOUBLE_LONG_WITH_SSI:
		return text

	# changes any occurrences of "ſſi" to "ſsi".
	pattern = r"ſſi"
	indices = [m.start() for m in re.finditer(pattern, text)]
	for i in indices:
		text = text[:i] + "ſs" + text[i + 2: ]

	return text


def spanish_conversion(text):
	USE_LONG_S_BEFORE_ACCENTED_O = False

	# selects every S that has a letter (or hyphen) after it,
	# so long as that letter is not B, F, nor H.
	clean_text = unidecode(text)
	pattern = r"s(?=[a-ac-eg-gi-zA-AC-EG-GI-Z-—])"
	indices = [m.start() for m in re.finditer(pattern, clean_text)]

	# excludes any S that occurs before an accented vowel.
	if USE_LONG_S_BEFORE_ACCENTED_O:
		pattern = r"s(?=[áàéèíìúùüÁÀÉÈÍÌÚÙÜ])"
	else:
		pattern = r"s(?=[áàéèíìóòúüÁÀÉÈÍÌÓÒÚÙÜ])"
	excluded_indices = [m.start() for m in re.finditer(pattern, text)]
	indices = [i for i in indices if i not in excluded_indices]
	for i in indices:
		text = text[:i] + "ſ" + text[i + 1: ]

	# changes any occurrences of "ſſi" to "ſsi".
	pattern = r"ſſi"
	indices = [m.start() for m in re.finditer(pattern, text)]
	for i in indices:
		text = text[:i] + "ſs" + text[i + 2: ]

	return text