
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

print("meep")
x = Person(1, "dead", "attack helicopter")
print(x.diagnosis)
y = Message(x, "hello")
print(y.content)

