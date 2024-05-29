#create program with meaning and install virtual environment 


import random  #first 
import randfacts  #thirdparty





fax = randfacts.get_fact()


a = int(random.randint(1,99))
b = int(random.randint(1,99))
c = int(random.randint(1,99))
d = int(random.randint(1,99))
e = int(random.randint(1,99))
f = int(random.randint(1,99))

z = int(random.randint(0,10))

lotterynumbers = [a,b,c,d,e,f]


fortunecookiesayings = ["Do not be afraid of competition.",
"An exciting opportunity lies ahead of you.",
"You love peace.",
"Get your mind set…confidence will lead you on.",
"You will always be surrounded by true friends.",
"Sell your ideas-they have exceptional merit.",
"You should be able to undertake and complete anything.",
"You are kind and friendly.",
"You are wise beyond your years.",
"Your ability to juggle many tasks will take you far.",
"A routine task will turn into an enchanting adventure."]


#final1 = cookie 
#final2 = cow fact 


def final():
    print(fortunecookiesayings[z] + " " + "Lottery Numbers:" + str(lotterynumbers) + "\nRandom Fact Cow Says: " + "" + fax )
    




