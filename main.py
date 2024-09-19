import os 
def main():
    path_to_file = "books/frankenstein.txt"
    book_title = os.path.splitext(os.path.basename(path_to_file))[0].capitalize()
    text_file = get_book_text(path_to_file)
    num_words = count_words(text_file)
    numbers_of_character= character_count(text_file)
    alphabetical_characters=filter_alphabetical_characters(numbers_of_character)
    alphabetical_characters_sorted=sorted(alphabetical_characters, reverse=True, key=sort_on)
    print(f"--- Begin report of books {book_title} ---")
    print(f"{num_words} words found in the document")
    for item in alphabetical_characters_sorted:
        for key, value in item.items():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")



def sort_on(box):
    return list(box.values())[0]

def filter_alphabetical_characters(dict):
    box =[]
    for key, value in dict.items():
        if key.isalpha():
            box.append({key:value})
    return box
          

def character_count(text):
    lower_string = text.lower()
    dictionary={}
    for symbols in lower_string:
        if symbols not in dictionary:
            dictionary[symbols] = 1
        else:
            dictionary[symbols] +=1
    return dictionary

  

def count_words(text):
        words = text.split()
        return len(words)  
          

def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except (FileNotFoundError, IOError):
        print(f"Ошибка при открытии файла: {path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return ""     
main()