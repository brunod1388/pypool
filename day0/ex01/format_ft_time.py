from datetime import datetime

date = datetime.now()
dateNum = date.timestamp()
comaNum = "{:,}".format(dateNum)
sciNum = "{:.2e}".format(dateNum)
print("Seconds since January 1, 1970: " + comaNum + " or " + sciNum)
print(datetime.fromtimestamp(dateNum).strftime("%b %d %Y"))