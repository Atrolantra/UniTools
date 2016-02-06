import requests
import re

synop_list = open("synopsis list.txt", "w")
def get_synopsis(unit):
	print "Getting synopsis for %s" % (unit)
	page = "https://www.qut.edu.au/study/unit-search/unit?unitCode=%s" % (unit)
	page_text = ((requests.get(page)).text).encode('utf-8')

	if '<h2>Unit not found</h2>' in page_text:
		return "Incorrect unit ID supplied.\n\n\n"
	try:
		synopsis = re.search(r"Synopsis:</H3>\n    <div>((.|\n)*?(?=</div>))", page_text)
		return (synopsis.group(1) + "\n\n")
	except AttributeError:
		return "No synopsis available\n\n\n"

units = open("ulist.txt", "r")
for unit in units.read().splitlines():
	synop_list.write(unit + ":\n")
	synop_list.write(get_synopsis(unit))