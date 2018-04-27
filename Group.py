import pickle
class Group:

    
    def __init__(self, group_name):

        self.group_name = group_name
        self.messages = []


    def __str__(self):

        return self.group_name

    def getMessages(self):

	output = "NONE"
	i=0
	for m in self.messages:
	
		if i==0:
			
			output = "\t" + m + "\n"
			i+=1
		else:

			output += "\t" +  m + "\n"


	return output

    def getGroupName(self):

        return self.group_name

    def getGroupMessages(self):

        return self.messages


    def addGroupMessage(self, message):

        self.messages.append(message)
        return self.messages

    def toString(self):

        String = self.group_name + "\n"
        size = self.messages.__len__()
        String += str(size) + "\n"

        for message in self.messages:

            String += message + "\n"

        return String

	








