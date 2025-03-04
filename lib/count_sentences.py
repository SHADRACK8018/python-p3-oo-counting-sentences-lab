import re
import sys

class MyString:
    def __init__(self, value=""):
        self.value = value  # Default value is an empty string
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")  # Print the error message instead of raising an exception
            self._value = ""  # You can assign an empty string or handle it however you'd like
    
    # Check if the string ends with a period (.)
    def is_sentence(self):
        return self.value.endswith(".")
    
    # Check if the string ends with a question mark (?)
    def is_question(self):
        return self.value.endswith("?")
    
    # Check if the string ends with an exclamation mark (!)
    def is_exclamation(self):
        return self.value.endswith("!")
    
    # Count the number of sentences in the string
    def count_sentences(self):
        # Use regular expression to split the string by sentence-ending punctuation
        sentences = re.split(r'[.!?]', self.value)
        # Filter out any empty strings from the split result
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return len(sentences)

# Test cases
string = MyString()
string.value = 123 
