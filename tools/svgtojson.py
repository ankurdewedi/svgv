import lxml.etree, re, json, argparse 

def q(o):
	element = []
	_a = {}
	for e in o:
		a = {
			'element':'',
			'attrs':{},
			'childrens':[],
		}
		a['element'] = e.tag
		if (e.attrib.get('class') != None):
			_a['attrs'] = {'class':e.attrib.get('class')}
		for ea in e.attrib :
			a['attrs'][ea] = e.attrib.get(ea)
		a['childrens'] = q(e)
		element.append(a)
	return element



def parse_svg(data):
	j = {}
	parser = lxml.etree.HTMLParser()
	tree = lxml.etree.fromstring(data, parser)
	tree = tree.xpath("body")
	for e in tree:
		j = q(e)
	j[0] = re.sub(r'\"([a-zA-Z]+)\"\:',r'\1:', json.dumps(j[0]) )

	j[0] = j[0].replace('[', '\n[\n\t');
	j[0] = j[0].replace('{', '\n{\n\t');
	j[0] = j[0].replace(']', '\n]\n');
	j[0] = j[0].replace('}', '\n}\n');
	j[0] = j[0].replace('}\n,', '\n},\n');
	j[0] = j[0].replace(']\n,', '\n],\n');

	print(j[0])

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input", type=str, help="Input Folder")
	args = parser.parse_args()
	if (args.input is not None):
		with open(args.input, 'r') as f:
			parse_svg(f.read())
