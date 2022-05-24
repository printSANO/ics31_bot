file = open('/Users/ryan/dev/ics31/chrome_extension/schedule.txt')
lines = file.readlines()
file.close()

for i in lines:
    j = i.split(',')
    print(j[0])