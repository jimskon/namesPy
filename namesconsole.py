# A test program for names stat lookup
from nameEntry import nameEntry
from nameMap import nameMap

def main():
	folder = "namedata/"
	femaleMap=nameMap(folder+'dist.female.first')
	maleMap=nameMap(folder+'dist.male.first')
	lastMap=nameMap(folder+'dist.all.last')
	
	t = "0"

	while (t in {"0","1","2"}):
		t = input("Enter type of search (0 for Female, 1 for Male, 2 for Last): ")
		name = input("Name to search for: ")
		name = name.upper()

		if t=="0":
			data=femaleMap.lookup10(name)
		elif t=="1":
			data=maleMap.lookup10(name)
		elif t=="2":
			data=lastMap.lookup10(name)
		else:
			print("No type entered")
		if data:
			print(data)
		else:
			printf("Nothing found")



main()