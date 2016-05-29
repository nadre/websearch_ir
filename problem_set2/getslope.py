#!/usr/bin/python

import sys
import urllib2
import matplotlib.pyplot as plt
from HTMLParser import HTMLParser

# small script that plots the token-tag slope curve of a given URL
# usage: "python2.7 getslope.py http://www.uni-weimar.de/en/media/chairs/webis/home/""

save_html = False

class HTMLSlopeParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.tag_count = 0
		self.token_count = 0
		self.in_script = False
		self.slope = []
		self.slope.append((0,0))

	def handle_starttag(self, tag, attrs):
		# print "Encountered a start tag:", tag
		if tag == "script":
			self.in_script = True
			return


	def handle_endtag(self, tag):
		# print "Encountered an end tag :", tag
		if tag == "script":
			self.in_script = False
			return
		if not self.in_script:
			self.tag_count += 1;
			last_token_count = self.slope[-1][0]
			self.slope.append((last_token_count, self.tag_count))

	def handle_data(self, data):
		# print "Encountered some data  :", data
		data = data.strip()
		if not self.in_script and data != "":
			last_tag_count = self.slope[-1][1]
			for word in data.split():
				print word
				self.token_count += 1;
				self.slope.append((self.token_count, last_tag_count))

def cleanupString(string, encoding):
    string = urllib2.unquote(string).decode(encoding)
    return HTMLParser().unescape(string)

if __name__ == '__main__':
	response = urllib2.urlopen(sys.argv[1])
	encoding = response.headers['content-type'].split("=")[-1]
	html = response.read()

	file_path = "dls/"+sys.argv[1].replace("/","")

	if save_html:
		pass
	with open(file_path+".html", "w") as text_file:
		text_file.write(html)

	html = cleanupString(html, encoding)

	parser = HTMLSlopeParser()
	parser.feed(html)
	
	last_point = parser.slope[-1]

	plt.scatter(*zip(*parser.slope))
	plt.axis([0, last_point[0], 0, last_point[1]])
	plt.title("slope curve\n"+sys.argv[1])
	plt.xlabel('tokens')
	plt.ylabel('tags')
	plt.savefig(file_path+".png")
	plt.show()