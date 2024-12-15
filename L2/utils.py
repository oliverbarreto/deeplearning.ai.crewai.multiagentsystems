# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

def get_serper_api_key():
    load_env()
    openai_api_key = os.getenv("SERPER_API_KEY")
    return openai_api_key


# break line every 80 characters if lsine is longer than 80 characters
# don't break in the middle of a word
def pretty_print_result(result):
    """
    Takes a string result and formats it for better readability by breaking long lines at 80 characters.
    
    This function:
    1. Splits the input string into lines
    2. For each line longer than 80 characters:
        - Splits it into words
        - Builds new lines by adding words while keeping line length <= 80 chars
        - Ensures words are not split in the middle
    3. Keeps shorter lines unchanged
    4. Joins all lines back together with newlines
    
    Args:
        result (str): The input string to format
        
    Returns:
        str: The formatted string with line breaks at 80 characters
    """
    parsed_result = []
    for line in result.split('\n'):
        if len(line) > 80:
            words = line.split(' ')
            new_line = ''
            for word in words:
                if len(new_line) + len(word) + 1 > 80:
                    parsed_result.append(new_line)
                    new_line = word
                else:
                    if new_line == '':
                        new_line = word
                    else:
                        new_line += ' ' + word
            parsed_result.append(new_line)
        else:
            parsed_result.append(line)
    return "\n".join(parsed_result)
