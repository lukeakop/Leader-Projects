def cakes(recipe, available):
    
    most_cakes_possible = 999999999  
    
    for ingredient in recipe:
        
        if ingredient in available:
            
            cakes_with_this_ingredient = available[ingredient] // recipe[ingredient]
            
            if cakes_with_this_ingredient < most_cakes_possible:
                
                most_cakes_possible = cakes_with_this_ingredient
        else:
            return 0

    return most_cakes_possible

"""
def cakes (recipe, available): განსაზღვრავს ფუნქციას, რომელიც იღებს ორ პარამეტრს:
recipe: ლექსიკონი, სადაც გასაღებები არის ინგრედიენტები და მნიშვნელობები - საჭირო რაოდენობა.
available: ლექსიკონი, სადაც გასაღებები არის ინგრედიენტები და მნიშვნელობები ხელმისაწვდომი ოდენობები.

"""

"""
მაქსიმალური ნამცხვრების ინიცირება:

most_cakes_possible = 999999999 ადგენს საწყის მაღალ მნიშვნელობას ნამცხვრების მაქსიმალური რაოდენობისთვის.

"""

"""
რეცეპტის ინგრედიენტების გამეორება:

for ingredient in recipe: მარყუჟები რეცეპტის თითოეულ ინგრედიენტში.

"""

"""

თუ ინგრედიენტი ხელმისაწვდომია: ამოწმებს, არის თუ არა არსებული ინგრედიენტი.

"""

"""
თუ ინგრედიენტი ხელმისაწვდომია, ის ითვლის რამდენი ნამცხვრის დამზადება შეიძლება ამ ინგრედიენტით: cakes_with_this_ingredient = available[ingredient] // recipe[ingredient]
// ოპერატორი ასრულებს მთელ რიცხვის დაყოფას, დამრგვალება ქვევით უახლოეს მთელ რიცხვამდე.

"""
"""

თუ ამჟამინდელი ინგრედიენტით შესაძლებელი ნამცხვრების რაოდენობა ნაკლებია ამჟამინდელ მაქსიმუმზე: if cakes_with_this_inredient < most_cakes_possible:
ის განაახლებს მაქსიმუმს: most_cakes_possible = cakes_with_this_ingredient

"""


