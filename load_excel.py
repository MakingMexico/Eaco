import petl as etl

def load():
	table = etl.io.xls.fromxls('stats.xls')
	print table

load()
