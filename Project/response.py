from Person import Person
from message import Message

def generateresponse(phonenumber, text):
    """
    Generate a response given a phone number and message

    :param phonenumber:
    :type phonenumber:
    :param message:
    :type message:
    :return:
    :rtype:
    """
    sender = Person(phonenumber)
    fm1 = Message(sender, text)
    sender.chatlog = [fm1]
    symptoms = sender.findSymptoms()
    possible_conditions = get_conditions(gender, age, )

