"""def human_years_cat_years_dog_years(human_years):
    if human_years == 1:                      
        return [1, 15, 15]
    
    elif human_years == 2:          
        return [2, 24, 24]
    
    else:
        return [human_years, 24 + (human_years - 2) * 4, 24 + (human_years - 2) * 5]
                

    return [0,0,0]"""


#თუ არგუმენტი human_years ტოლია ან უდრის ერთს დავაბრუნოთ წლები კატის და ძაღლის ლისტის სახით
#შემდეგ კატის წლოვანება გავზარდეთ მეორე წელს +9-ით და გამოვიდა 24-ი რადგან პირველი წლის 15ს მივუმატეთ 9 წელი