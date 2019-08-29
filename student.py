
class Student():


    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return None

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return None

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0

    @property
    def full_name(self):
        try:
            return self.__first_name + " " + self.__last_name
        except AttributeError:
            return None

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a first name')

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a last name')

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Please provide a whole number for age")

    @cohort.setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError("Please provide a whole number for age")
s = Student()
s.first_name = "Scott"
s.last_name = "Silver"
print(s.full_name)







# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.