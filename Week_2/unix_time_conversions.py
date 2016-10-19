import time, datetime

def readable_to_unix(date_text):
	while True:
		try:
			unix_time = time.mktime(datetime.datetime.strptime(str(date_text), "%d-%m-%Y").timetuple())
			return unix_time
			break
		except ValueError:
			print("Date input in an incorrect format. Correct format is DD-MM-YYYY, where D=day, M=Month, Y=Year")
			date_text = input ("Please input correct date format: ")


def unix_to_readable(unix_time):
	readable_time = datetime.datetime.fromtimestamp(int(unix_time)).strftime('%d-%m-%Y')
	return readable_time