#Question 6

#import dependency
import re
import datetime

#initialise filepath
input_filepath = "6-CountDates.txt"
#input_filepath = input("Please enter your text filepath: ")

def countDates(txt_filepath):
	re_pattern = "(\\b(([0-9])|([0-2][0-9])|([3][0-1])) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-9]{4}\\b)|(\\b(0[1-9]|[12][0-9]|3[01])\\/(0[1-9]|1[012])\\/[0-9]{4}\\b)|(\\b(0[1-9]|1[012])\\/(0[1-9]|[12][0-9]|3[01])\\/[0-9]{4}\\b)|(\\b[0-9]{4}\\/(0[1-9]|1[012])\\/(0[1-9]|[12][0-9]|3[01])\\b)"
	fmts = ["%Y/%m/%d","%m/%d/%Y","%d/%m/%Y","%d %b %Y"]
	with open(txt_filepath) as f:
		text = f.read()
		matches = re.findall(re_pattern, text)
	# To parsing as date to handle invalid dates that pass the regex check e.g. 31 Feb 2021
	counter = 0	
	for match in matches:
		str_match = next(s for s in match if s)
		for fmt in fmts:
			try:
				datetime.datetime.strptime(str_match, fmt)
				counter += 1
			except:
				continue
	return (counter)

print(countDates(input_filepath))

