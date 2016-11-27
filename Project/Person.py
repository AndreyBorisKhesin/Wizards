from Message import Message
from Symptoms import Symptoms

class Person:

    def __init__(self, phone_number, diagnosis, gender,
                 chatlog = [], name = "Anon"):
        """
        Instantiate an instance of a Person.

        :param phone_number: int
            The phone number of this person
        :param name: str
            The name of this person
        :type name:
        :param diagnosis: Diagnosis
            The diagnosis
        :param gender: str
            The gender of this person
        :param chatlog: List of Messages

        :rtype: None
        """
        self.phone_number = phone_number
        self.diagnosis = diagnosis
        self.gender = gender
        self.name = name
        self.chatlog = chatlog

    def findSymptoms(self):
        """
        Returns a list of reported symptoms from the individual's
        chatlog.

        :rtype: List[String]
            A list of all symptoms.
        """
        output = []
        for msg in self.chatlog:
            if msg.p == self:
                i = 0
                while i < len(msg.content):
                    if msg.content[i] == "#":
                        newsymp = ""
                        j = i + 1
                        while j < (len(msg.content)):
                            newsymp = newsymp + msg.content[j]
                            if (msg.content[j] == "#"):
                               if newsymp != "#":
                                    l = len(newsymp) - 1
                                    newsymp = newsymp[0:l]
                                    output.append(newsymp.lower())
                                    i = j + 1
                                    break
                            j = j + 1
                    i = i + 1

        """
        for s in output:
            if s == " ":
                output.remove(s)
        """
        return output

    def getSymptomCodes(self):
        symptoms = self.findsymptoms()
        s = Symptoms
        keys = []
        for i in symptoms:
            keys.append(s.getSymptomKey(i))



if __name__ == "__main__":
    p1 = Person("0", "Alive", "Male")
    m1 = Message(p1, "SOS #MissiNg eYeBALL# #HeAdache# #decapitated# SOS")
    p1.chatlog = [m1]
    p1.name = "Isaac"
    for c in p1.findSymptoms():
        print(c)
    print(p1.findSymptoms())