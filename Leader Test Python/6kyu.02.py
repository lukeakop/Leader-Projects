"""def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_backwards_prime(n):
    str_n = str(n)
    reversed_n = int(str_n[::-1])
    return is_prime(n) and is_prime(reversed_n) and n!= reversed_n

def backwards_prime(start, stop):
    return [n for n in range(start, stop + 1) if is_backwards_prime(n)]"""

#if n < 2: return False: თუ n ნაკლებია 2-ზე, ეს არ არის მარტივი რიცხვი, ამიტომ ვაბრუნებთ False.
#i-სთვის დიაპაზონში(2, int(n ** 0.5) + 1): ჩვენ ვიწყებთ ციკლს 2-დან n-ის კვადრატულ ფესვამდე (მათ შორის). 
#ჩვენ ვიყენებთ int(n ** 0.5) + 1, რათა თავიდან ავიცილოთ შემოწმება კვადრატული ფესვის მიღმა.

#მეორე  ხაზზე ჩვენ ვქმნით ასოების შემობრუნების ფუქციას.

#და ბოლოს ფუნქცია აბრუნებს ყველა n რიცხვის ჩამონათვალს დასაწყისიდან გაჩერებამდე დიაპაზონში (მათ შორის), 
#რომლებიც არის უკუღმა მარტივი რიცხვები, როგორც ეს არის განსაზღვრული is_backwards_prime ფუნქციით.