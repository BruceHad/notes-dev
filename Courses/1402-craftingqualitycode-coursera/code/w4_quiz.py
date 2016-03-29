class Contact:
    """ A contact with a first name, a last name, and an email address. """

    def __init__(self, first_name, last_name, email_address):
        """ (Contact, str, str, str) -> NoneType 

        Initialize this Contact with first name first_name, last name 
        last_name, and email address email_address.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def __str__(self):
        """ (Contact) -> str
 
        Return a string representation of this contact.
        """

        return '{0} {1} <{2}>'.format(self.first_name, 
            self.last_name, self.email_address)

    def add_phone_number(self, telephone_num):
        """ (Contact, str) -> NoneType

        Add phone number telephone_num for this contact.
        """

        self.phone_number = telephone_num

class Email:
    """ An email with a list of recipients, a subject and a body. """

    def __init__(self, recipients, subject, body):
        """ (Email, list of Contact, str, str) -> NoneType

        Initialize this Email with recipients, subject and body.
        """

        self.recipients = recipients
        self.subject = subject
        self.body = body

    def __str__(self):
        """ (Email) -> str

        Return a string representation of this email.
        """
      
        result = 'To: '
        for contact in self.recipients:
            result = result + '{0}, '.format(contact)

        result = result + '\nSubject: {0}'.format(self.subject)
        result = result + '\n{0}'.format(self.body)
        return result