import re

top_meals =  ['Meal ID: 35,Food Item Name: Biryani Average Rating: 5.0, Sentiment Score: 1.0, , Category: Lunch', 'Meal ID: 37,Food Item Name: Paneer Tikka Average Rating: 5.0, Sentiment Score: 0.0, , Category: Lunch', 'Meal ID: 39,Food Item Name: Samosa Average Rating: 4.0, Sentiment Score: 1.0, , Category: Breakfast', 'Meal ID: 36,Food Item Name: Dosa Average Rating: 3.0, Sentiment Score: 0.0, , Category: Breakfast', 'Meal ID: 40,Food Item Name: Gulab Jamun Average Rating: 4.5, Sentiment Score: -0.5, , Category: Dinner', 'Meal ID: 59,Food Item Name: Dum Aloo  Average Rating: 3.5, Sentiment Score: -0.5, , Category: Dinner']


meal_id_pattern = r'Meal ID: (\d+)'
category_pattern = r'Category: (\w+)'

for meal in top_meals:
    print("meal: ", meal)
    
    meal_id_match = re.search(meal_id_pattern, meal)
    category_match = re.search(category_pattern, meal)
    
    if meal_id_match and category_match:
        meal_id = meal_id_match.group(1)
        category = category_match.group(1)
        
        date = datetime.date.today()
        chef_id = "5"
        
        cursor.execute("""
            INSERT INTO Recommendation (date, chefID, foodItemID, category)
            VALUES (%s, %s, %s, %s)
        """, (date, chef_id, meal_id, category))

        print(f"Meal ID {meal_id} broadcasted to employees.")
    else:
        print(f"Could not extract information from meal: {meal}")