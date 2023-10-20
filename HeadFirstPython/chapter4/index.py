

# with open('james.txt') as jaf: data=jaf.readline()
# james=data.strip().split(',')

# with open('julie.txt') as juf: data=juf.readline()
# julie=data.strip().split(',')

# with open('mikey.txt') as mif: data=mif.readline()
# mikey=data.strip().split(',')

# with open() as saf: data=saf.readline()
# sarah=data.strip().split(',')

cleese={}
palin=dict()
cleese['Name']='John cleese'
cleese['Occupations']=['actor','comedian','writer','film producer']

palin={'Name':'Michael palin','Occupations':['comedian','actor','writer','tv']}
palin['BirthPlace']="Broomhill,sheffield,england"
cleese['BirthPlace']="Weston-super-Mare,North Somrset,england"


def get_coach_data(filename):
	try:
		with open(filename) as jaf: data=jaf.readline()
		templ=data.strip().split(',')

		return({'Name':templ.pop(0),
				'DOB':templ.pop(0),
				'Times':str(sorted(set([sanitize(t) for t in templ]))[0:3])
					})

	except IOError as ioerr:
		print("error is :"+ str(ioerr))
		return(None)

def sanitize(time_string):
	if '-' in time_string:
		splitter='-'
	elif ':' in time_string:
		splitter=':'
	else :
		return(time_string)

	(mins,secs)=time_string.split(splitter)
	return(mins+'.'+secs)
sarah=get_coach_data('sarah2.txt')

print(sarah)

'''(sarah_name,sarah_dob)=sarah.pop(0),sarah.pop(0)
print(sarah_name+"'s faster time are:"+str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
james=get_coach_data('james.txt')
julie=get_coach_data('julie.txt')
mikey=get_coach_data('mikey.txt')
sarah=get_coach_data('sarah.txt')

james=sorted(set([sanitize(each_t) for each_t in james]))[0:3]
julie=sorted([sanitize(each_t) for each_t in julie])
mikey=sorted([sanitize(each_t) for each_t in mikey])
sarah=sorted([sanitize(each_t) for each_t in sarah])
print(james)
unique_james=[]
for each_t in james:
	if each_t not in unique_james:
		unique_james.append(each_t)

unique_julie=[]
for each_t in julie:
	if each_t not in unique_julie:
		unique_julie.append(each_t)

unique_mikey=[]
for each_t in mikey:
	if each_t not in unique_mikey:
		unique_mikey.append(each_t)
unique_sarah=[]
for each_t in sarah:
	if each_t not in unique_sarah:
		unique_sarah.append(each_t)

print(unique_james[0:3])

print(unique_sarah[0:3])
print(unique_mikey[0:3])
print(unique_julie[0:3])
'''
