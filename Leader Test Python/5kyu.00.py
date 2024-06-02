"""def generate_hashtag(s):
    if not s or len(s) == 0:
        return False
    
    
    hashtag = '#' + ''.join(word.capitalize() for word in s.split())
    
    
    if len(hashtag) > 140:
        return False
    
    return hashtag"""

#if not s ან len(s) == 0:: ეს ამოწმებს შეყვანის სტრიქონი ცარიელია თუ None. თუ ასეა, ფუნქცია აბრუნებს False-ს.
#hashtag = '#' + ''.join(word.capitalize() word in s.split()): ეს ხაზი ქმნის ჰეშთეგის სტრინგს.
#if len(hashtag) > 140:: ეს ამოწმებს სტრინგი ცარიელია თუ None. თუ ასეა, ფუნქცია აბრუნებს False-ს.