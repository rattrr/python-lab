import re

regex_email = re.compile(
  r'''(?P<adres>
    (?P<login>[\w+.]+)@(?P<domena>\w+(\.\w+)+)
  )''',
  re.IGNORECASE | re.VERBOSE
)

class Email(object):
    def __init__(self, email):
        if regex_email.match(email):
            self.email = email
        else:
            raise ValueError("Not an email")
    def __repr__(self):
        return self.email

try:
    print Email("testasdf.@jcom")
except ValueError as err:
    print err
