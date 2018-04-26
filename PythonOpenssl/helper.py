import Group as g



def write_group_content(groups):

    f = open("groups.txt","w")

    for group in groups:

        f.write(group.toString())


    f.write("#EOF")
    f.close()

def read_group_content(groups):

    f = open("groups.txt")

    line = f.readline().strip()

    while  (line != "#EOF"):

        #name
        temp = g.Group(line.strip())

        size = int(f.readline().strip())
        i =0
        while (i < size):

            temp.addGroupMessage(f.readline().strip())
            i +=1

        #print "\n--------------\n"
        groups.append(temp)

        #new line
        line = f.readline().strip()



    #print "Complete"
    return groups



'''
group1 = g.Group("Group1")
group1.addGroupMessage("Yo What up Dawg")
group1.addGroupMessage("YOOOO")


group2 = g.Group("Group2")
group2.addGroupMessage("Yo What up Dawg")
group2.addGroupMessage("YOOOO")
group2.addGroupMessage("Hello There")
group2.addGroupMessage("What up dawg")

groups = [group1 , group2]



write_group_content(groups)

groups = []
groups = read_group_cotent(groups)

for group in groups:

    print group.getGroupName()
    print group.messages
'''



