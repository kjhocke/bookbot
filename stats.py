def get_word_count(file_contents):
    split_contents = file_contents.split()
    word_count = len(split_contents)
    return word_count

def get_character_count(file_contents):
    lowercase_adjusted_contents = file_contents.lower()
    character_list = list(lowercase_adjusted_contents)
    character_dictionary = {}
    
    for character in character_list:
        
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    
    return character_dictionary

def sort_dictionary(dictionary):
    
    sorted_dictionary_list = []

    for character in dictionary:
        if character.isalpha() == True:
            sorted_dictionary_list.append({"char": character, "num": dictionary[character]})
    
    sorted_dictionary_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_dictionary_list