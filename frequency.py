from stop_word import stopwords
import string
def calculate_frequency(content):
    """
    Function to calculate frequency of each word in the content
    :param content: String from which frequency of each word is calculated
    :return: dictionary consisting of unique words as key and
            their frequenct as values
    """
    #Remove the special characters from the contents
    new_content = ""
    for char in content:
        if char in string.punctuation:
            continue
        new_content+=char.lower()
    result = {}     #dictionary consisting of words as key and their frequency as values

    #Convert the string new_content to list
    #It will be easier to count words
    content_list = new_content.split(" ")
    content_list = [element for element in content_list if element != ""]
    for word in content_list:
        if word in stopwords:
            continue
            #Since we don't want to add stopwords in our dictionary

        if word in result.keys():
            result[word]+=1
            #If word already exists in dictionary increase its frequency by 1
        else:
            result[word]=1
            #If word does not exist in dictionary then add it to dictionary
    result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1],reverse = True)}
    #sorting the dictionary in decending order acc to values
    return result