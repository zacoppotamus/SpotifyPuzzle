#Zac Ioannidis, 2012
#!/usr/bin/python

from sys import argv
import calendar
from datetime import date
from itertools import permutations

def possibleDates (a,b,c):
	all_dates = []
	for a,b,c in permutations([a,b,c]):
		try:	
			d=date(a,b,c)
			if isValidDate(d)==True:
				if len(str(a))<4:
					a=a+2000
					d=date(a,b,c)
				all_dates.append(d.isoformat())
			else:
				continue
		except ValueError:
			continue
	return all_dates

def isValidDate (d):
	MIN_YEAR=2000
	MAX_YEAR=2999

	if d.year<MIN_YEAR:
		if d.year+MIN_YEAR>MAX_YEAR:
			return False
	elif d.year>MAX_YEAR:
		return False

	if d.month<=12:
		l=calendar.monthrange(d.year,d.month)
		if l[1]<int(d.day):
			return False
	else:
		return False

	return True

if __name__=='__main__':
	#convert input to numbers
	data=raw_input()
	try:	
		a,b,c=map(int,data.split("/"))
		dates=possibleDates(a,b,c)
		try:	
			print min(dates)
		except ValueError:
			print "%s is illegal"% data
			exit()
	except ValueError:
		print "%s is illegal"% data
		exit()
