from message import Message
from Person import*
class Response:
    people = []

    def generateresponse(phonenumber, text, time):
        """
        Generate a response given a phone number and message

        :param phonenumber: int
                The person's phone number
        :param text: str
                The person's message
        :rtype: str
        """
        found = False
        for peeps in Response.people:
            if peeps


