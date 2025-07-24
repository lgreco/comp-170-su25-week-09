from Birthday import Birthday


class Person:

    def __init__(self, first_name, last_name):
        """A person is defined by a first and last name, a birthday in the 
        form (month, day), and a city they live in. Additional fields may 
        be added here later. A new object requires only a first and last 
        name to instatiate. The remaining fields can be set later using 
        the corresponding mutator methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = None
        self.city = None

    def introduce(self):
        """Simple way for a person object to introduce itself."""
        print(
            f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}"
        )

    def set_birthday(self, month, day):
        """Mutator for birthday. Uses our very own Birthday class."""
        self._birthday = Birthday(month, day)

    def set_city(self, city):
        """Mutator for city."""
        self.city = city

    def get_first_name(self):
        """Accessor for first name"""
        return self.first_name

    def get_last_name(self):
        """Accessor for last name"""
        return self.last_name

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.first_name} {self.last_name}]"


    def say_birthday(self):
        # ordinal indicators
        st = [1,21,31] # these days are ordinally indicated "st"
        nd = [2, 22] # these days are ordinally indicated "nd"
        rd = [3, 23] # these days are ordinally indicated "rd"
        # month names
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        ordinal_indicator = "th" # default ordinal indicator
        if self.day in st: ordinal_indicator = "st"
        if self.day in nd: ordinal_indicator = "nd"
        if self.day in rd: ordinal_indicator = "rd"
        # Break down birthday data for reability
        day = self.birthday.get_day()
        month = self.birthday.get_month()
        return f"{day}{ordinal_indicator} of {months[month-1]}"

    def __lt__(self, other):
        # Simply delegate the comparison to the strings in question
        return self.first_name < other.first_name