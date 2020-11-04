q= [
	"How many continents are there?",  			# pehla question
	"What is the capital of India?",			# doosra question
	"NG mei kaun se course padhaya jaata hai?"	# teesra question
]

o= [
	#pehle question ke liye options
	["Four", "Nine", "                                                                                                                                                                                                                                          ", "Eight"],
	#second question ke liye options
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	#third question ke liye options
	["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
fifty=[[3,1],[1,4],[1,3]]
s=[3,4,1]
hint=0
i=0
while i<len(q):
    print(q[i])
    j=0
    while j<len(o[i]):
        print(j+1,o[i][j])
        j=j+1
    chance=int(input("enter the chance/ans :"))
    if hint==0:
        if chance==50:
            k=0
            while k<len(fifty[i]):
              print("option",fifty[i][k])
              k=k+1
            ans2=int(input("enter ans"))
            if ans2==s[i]:
               print("congress")
            else:
               print("wrong")
               break
            hint=hint+1
        elif chance==s[i]:
            print("congress")
        else:
            print("wrong")
            break
            
    else:
        print("chance khtm")
        chance=int(input("enter again ans"))
        if chance==s[i]:
            print("congress")
        else:
            print("wrong")
            break     
    print()
    i=i+1
     