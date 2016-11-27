class Message:

    def __init__(self, p, content):
        """
        Instantiate a message

        :param p: Person
            The sender of this message
        :param content: String
            The contents of this message.
        :rtype: None
        """
        self.p = p
        self.content = content
