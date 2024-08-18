def encode(word):
    vowel_code = {
        'a': '1',
        'e': '2',
        'i': '3',
        'o': '4',
        'u': '5'
    }
    
    encoded_word = ""
    
    for letter in word:
        if letter in vowel_code:
            encoded_word += vowel_code[letter]
        else:
            encoded_word += letter
    
    return encoded_word

def decode(secret_word):
    number_to_vowel = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }
    
    decoded_word = ""
    
    for char in secret_word:
        if char in number_to_vowel:
            decoded_word += number_to_vowel[char]
        else:
            decoded_word += char
    
    return decoded_word

"""
encode ფუნქცია სიტყვაში ხმოვანებს ცვლის რიცხვებით (a:1, e:2, i:3, o:4, u:5) dictionary mapping გამოყენებით.

ის იმეორებს თითოეულ ასოს, ანაცვლებს ხმოვანებს მათი შესაბამისი რიცხვებით და თანხმოვნები უცვლელი რჩება.

"""

"""
decode ფუნქცია აკეთებს საპირისპიროს, აბრუნებს რიცხვებს ხმოვანებად მსგავსი dictionary-ს გამოყენებით.

ორივე ფუნქცია ქმნის ახალ სტრინგიან სიმბოლოს სიმბოლოს მიხედვით, აბრუნებს დაშიფრულ ან დეკოდირებულ შედეგს.

"""
