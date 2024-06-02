"""def variance(numbers):
    
    mean = sum(numbers) / len(numbers)

    
    squared_diffs = []
    for num in numbers:
        diff = num - mean
        squared_diff = diff ** 2
        squared_diffs.append(squared_diff)

    
    variance = sum(squared_diffs) / len(numbers)

    return variance"""

#mean = sum (numbers) / len (numbers) ეს ხაზები ითვლის შეყვანის სიის რიცხვების საშუალოს (საშუალოდ). 
#ჯამის ფუნქცია აგროვებს სიაში არსებულ ყველა რიცხვს და შედეგი იყოფა სიის სიგრძეზე (ანუ ელემენტების რაოდენობაზე) საშუალოს მისაღებად.

#Squared_diffs = [],  squared_diffs.append(squared_diff) ეს ხაზები ითვლის კვადრატულ განსხვავებებს საშუალოდან. 
#კოდი მოძრაობს შეყვანის სიაში თითოეულ რიცხვში, აკლებს საშუალოს რიცხვს სხვაობის მისაღებად, 
#კვადრატში აქცევს სხვაობას (ანუ ამაღლებს მას 2-ის ხარისხზე) და კვადრატულ განსხვავებას უერთებს სიას სახელწოდებით Squared_diffs.