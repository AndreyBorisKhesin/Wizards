from message import Message
from Person import*


class Response:
    people = []

    @staticmethod
    def generateresponse(phonenumber, textmessage, timestamp):
        """
        Generate a response given a phone number and message

        :param phonenumber:
        :type phonenumber:
        :param message:
        :type message:
        :return:
        :rtype:
        """
        textmessage1 = textmessage.lower()
        found = False
        for p in range(len(Response.people)):
            if Response.people[p].phone_number == phonenumber:
                found = True
                cpeep = Response.people[p]
        if (not found):
            newp = Person(phonenumber)
            Response.people.append(newp)
            cpeep = newp
        i = 0
        while i < len(msg.content):
            if textmessage1 == "#":
                newsymp = ""
                    j = i + 1
                    while j < (len(msg.content)):
                        newsymp = newsymp + textmessage1[j]
                        if (msg.content[j] == "#"):
                            if newsymp != "#":
                                l = len(newsymp) - 1
                                newsymp = newsymp[0:l].lower()
                                if not cpeep.symptoms.__contains__(newsymp):
                                    cpeep.symptoms.append(newsymp)
                                i = j + 1
                                break
                        j += 1
                i += 1
        if cpeep.gender == "":
            if textmessage1 == "f" or textmessage1 == "m":
                cpeep.gender = textmessage1
            else:
                return "What is your gender? Please enter F for Female and M for Male"
        if cpeep.gender != "" and cpeep.age == -1:
            try:
                age = int(textmessage1)
                if age >= 0:
                    cpeep.age = age
                else:
                    return "How old are you?"
            except ValueError:
                return ("How old are you?")
        if cpeep.gender != "" and cpeep.age >= 0:
            return "Please enter all relevant symptoms. Symptoms should be between two hashes, for instance, #headache#."

if __name__ == "__main__":
    print(Response.generateresponse(11, "I'm dying, help!", 0))
    print(Response.generateresponse(11, "2", 0))
    print(Response.generateresponse(11, "M", 0))
    print(Response.generateresponse(11, "2", 0))
    print(Response.generateresponse(11, "#headache#", 0))
