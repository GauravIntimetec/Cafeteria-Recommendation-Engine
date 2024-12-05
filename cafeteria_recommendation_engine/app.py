# from models.user import User
# from models.admin import Admin
# from models.chef import Chef
# from models.employee import Employee
from utils.db_utils import init_db

def main():
    # create_tables()
    init_db()
    
    print("Welcome to the Cafeteria Recommendation Engine")
    print("Please log in:")
    user_id = input("Enter your user ID: ")
    name = input("Enter your name: ")
    
    user = User.login(user_id, name)
    
    if user:
        if isinstance(user, Admin):
            admin_dashboard(user)
        elif isinstance(user, Chef):
            chef_dashboard(user)
        elif isinstance(user, Employee):
            employee_dashboard(user)
    else:
        print("Invalid credentials")

def admin_dashboard(admin):
    while True:
        print("\nAdmin Dashboard")
        print("1. Add Meal")
        print("2. Remove Meal")
        print("3. Update Meal")
        print("4. Change Price")
        print("5. Update Availability")
        print("6. Log Out")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            admin.add_meal()
        elif choice == '2':
            admin.remove_meal()
        elif choice == '3':
            admin.update_meal()
        elif choice == '4':
            admin.change_price()
        elif choice == '5':
            admin.update_availability()
        elif choice == '6':
            break

def chef_dashboard(chef):
    while True:
        print("\nChef Dashboard")
        print("1. View Notifications")
        print("2. View Algo Recommended Meals")
        print("3. Rollout Option")
        print("4. Publish Monthly Report")
        print("5. View Today's Meal")
        print("6. View Ratings of Menu")
        print("7. Log Out")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            chef.view_notifications()
        elif choice == '2':
            chef.view_algo_recommended()
        elif choice == '3':
            chef.rollout_option()
        elif choice == '4':
            chef.publish_report()
        elif choice == '5':
            chef.view_today_meal()
        elif choice == '6':
            chef.view_ratings()
        elif choice == '7':
            break
        else:
            print("Invalid option")

def employee_dashboard(employee):
    while True:
        print("\nEmployee Dashboard")
        print("1. View Notifications")
        print("2. View Today's Menu")
        print("3. Vote for Tomorrow's Meal")
        print("4. Provide Feedback and Rating")
        print("5. Log Out")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            employee.view_notifications()
        elif choice == '2':
            employee.view_todays_menu()
        elif choice == '3':
            employee.vote()
        elif choice == '4':
            employee.provide_feedback()
        elif choice == '5':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
