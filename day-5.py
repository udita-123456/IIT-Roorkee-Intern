#create a phonebook(dict):add,searchdelete contacts\
phonebook = {}
while True:
    print("\nPhonebook Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print("Contact added successfully!")
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print("Contact not found!")
    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")
    elif choice == "4":
        if phonebook:
            print("\nContacts:")
            for name, number in phonebook.items():
                print(f"{name}: {number}")
        else:
            print("Phonebook is empty!")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")






#count word frequency in a sentence using a dictionary
sentence="my name is udita"
words=sentence.split()
freq={}
for word in words:
    freq[word]=freq.get(word,0)+1
print(freq)







#find unique characters in a string using sets
string = input("Enter a string: ")
unique_chars =sorted(set(string))
print("Unique characters are:",unique_chars)



#or
string = input("Enter a string: ")
unique_chars =sorted(set(string))
print("Unique characters are:")
for char in unique_chars:
    print(char, end=" ")








#build a word reversal and palindrome checker
word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)
if word.lower() == reversed_word.lower():
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")








#student report card:dict of name->{marks,grade}
report_card={"chetna":{"marks":78,"grade":"C"},"bharti":{"marks":87,"grade":"B"},"varsha":{"marks":56,"grade":"F"},"shivani":{"marks":68,"grade":"D"}}
print(report_card["chetna"])








#anagram checker using sorted strings or sets
def are_anagrams(str1,str2):
    return sorted(str1)==sorted(str2)
print(are_anagrams("listen","silent"))
print(are_anagrams("hello","world"))








#caesar cipher encoder/decoder
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

encoded = caesar_cipher(input("enter the name"), 3)
decoded = caesar_decipher(encoded, 3)

print("Encoded:", encoded)
print("Decoded:", decoded)