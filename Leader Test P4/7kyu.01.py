def is_divisible(*numbers):
    number_to_check = numbers[0]
    
    for divisor in numbers[1:]:
        if number_to_check % divisor != 0:
            return False
    
    return True


"""
ფუნქციის განმარტება:

ფუნქცია განისაზღვრება *numbers, როგორც მისი პარამეტრი. ვარსკვლავი (*) 
საშუალებას აძლევს ფუნქციას მიიღოს ნებისმიერი რაოდენობის არგუმენტები, 
რომლებიც შეფუთული იქნება tuple-ში, რომელსაც ეწოდება რიცხვები.

"""

"""
შესამოწმებლად ნომრის ამოღება:

number_to_check = numbers[0]: პირველი რიცხვი რიცხვების წყებაში ენიჭება number_to_check-ს. 
ეს არის რიცხვი, რომელიც შემოწმდება გასაყოფად.

"""