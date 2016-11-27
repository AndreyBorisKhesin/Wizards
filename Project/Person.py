import Symptoms

class Person:

    def __init__(self, phone_number=""):
        """
        Instantiate an instance of a Person.

        :param phone_number: str
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
        self.gender = ""
        self.age = -1
        self.symptoms = []

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

    def getSymptomCodes(self):
        """
        :return: the list of API codes corresponding to each of the
		symptoms the patient described
        :rtype: list[String]
        """
        self.findSymptoms()
        s = Symptoms.Symptoms()
        keys = []
        for i in self.symptoms:
            key = s.getSymptomKey(i)
            keys.append(key)
        return keys

'''
if __name__ == "__main__":
    p1 = Person("0")
    p1.gender = "f"
    p1.age = 20
'''


