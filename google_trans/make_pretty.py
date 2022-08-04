from bs4 import BeautifulSoup
import bs4

customFormatter = bs4.formatter.XMLFormatter(indent=4, )

filename = "texts_zh.xml"
infile = open(filename, "r", encoding="utf-8")
bs = BeautifulSoup(infile, 'xml')
pretty_xml = bs.prettify(formatter=customFormatter)

infile.close()

outfile = open(filename, "w", encoding="utf-8")
outfile.write(pretty_xml)
outfile.close();
