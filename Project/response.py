import Message
import Person


class Response:
    people = []

    @staticmethod
    def generateresponse(phonenumber, textmessage, timestamp):
        """
        Generate a response given a phone number and message

        :param phonenumber: string
        :param message: string
        :return:
        """
        textmessage1 = textmessage.upper()
        found = False
        # Check if the person exists in the list of people
        for p in range(len(Response.people)):
            if Response.people[p].phone_number == phonenumber:
                found = True
                # current person
                cpeep = Response.people[p]
        if (not found):
            newp = Person(phonenumber)
            Response.people.append(newp)
            cpeep = newp
        if cpeep.gender == "":
            if textmessage1 == "F" or textmessage1 == "M":
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
