def going(n):
    top_number = 0
    bottom_number = 1
    
    for i in range(1, n + 1):
        bottom_number = bottom_number * i
        
        top_number = top_number + bottom_number
    
    result = top_number / bottom_number
    
    result_string = str(result)
    
    if '.' in result_string and len(result_string.split('.')[1]) > 6:
        result_string = result_string[:result_string.index('.') + 7]
    
    return float(result_string)


"""
  1. დავადეკლარირეთ ფუქნცია სახელად going რომელსაც გავუწერეთ პარამეტრი n

  2. top_number = 0 და bottom_number = 1 ახდენს ჩვენი წილადის მრიცხველისა და მნიშვნელის ინიციალიზებას.

  3. ციკლი i დიაპაზონში (1, n + 1): მეორდება 1-დან n-მდე.
    თითოეულ გამეორებაში:
    bottom_number = bottom_number * i ითვლის i-ის ფაქტორიალს.
    top_number = top_number + bottom_number ამატებს ამ ფაქტორიალს გაშვებულ ჯამს.

  4. result = top_number / bottom_number ყოფს ჯამს საბოლოო ფაქტორიალზე.
  
"""

