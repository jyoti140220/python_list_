# ask question and user give answer
q= [
	"How many continents are there?",  			# pehla question
	"What is the capital of India?",			# doosra question
	"NG mei kaun se course padhaya jaata hai?"	# teesra question
]

o= [
	#pehle question ke liye options
	["Four", "Nine", "Seven", "Eight"],
	#second question ke liye options
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	#third question ke liye options
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
s=[3,4,1]
i=0
while i<len(q):
    print(q[i])
    j=0
    while j<len(o[i]):
        print(j+1,o[i][j])
        j=j+1
    ans=int(input("enter ans :"))
    if ans==s[i]:
    	print("congress")
    else:
    	print("wrong")
    
    print()
    i=i+1