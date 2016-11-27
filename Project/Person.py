import Message
import Symptoms

class Person:

    def __init__(self, phone_number=-1):
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

    '''
    def __init__(self, phone_number=-1, gender = "", age=-1, symptoms = []):
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
        self.gender = gender
        self.age = age
        self.symptoms = []
    '''

    def findSymptoms(self):
        """
        Returns a list of reported symptoms from the individual's
        chatlog.

        :rtype: None
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
                                    newsymp = newsymp[0:l].lower()
                                    if not self.symptoms.__contains__(newsymp):
                                        self.symptoms.append(newsymp)
                                    i = j + 1
                                    break
                            j = j + 1
                    i = i + 1


        return output

    def getSymptomCodes(self):
        """
        :return: the list of API codes corresponding to each of the symptoms the patient described
        :rtype: list[String]
        """
        self.findSymptoms()
        s = Symptoms()
        keys = []
        for i in self.symptoms:
            key = s.getSymptomKey(i)
            keys.append(key)
        return keys

if __name__ == "__main__":
    p1 = Person("0", "Alive", "Male")
    m1 = Message(p1, "SOS #sNoring# #Abdominal pain# #black StOOls# SOS")
    p1.chatlog = [m1]
    p1.name = "Isaac"
    print(p1.getSymptomCodes())
    print(p1.symptoms)
