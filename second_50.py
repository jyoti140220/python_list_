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
fifty=[[3,1],[1,4],[1,3]]
s=[3,4,1]
i=0
while i<len(q):
    print(q[i])
    j=0
    while j<len(o[i]):
        print(j+1,o[i][j])
        j=j+1
    ans=input("enter the 50-50/select ans :")
    if ans=="50-50":
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
    elif ans=="select ans":
    
        choose=int(input("enter your ans"))
        if choose==s[i]:
            print("congress")
        else:
            print("wrong")
            break
        print()
        i=i+1

    
