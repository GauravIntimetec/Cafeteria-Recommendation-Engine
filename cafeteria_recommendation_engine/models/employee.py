from .user import User
from .notification import Notification
from .menu_item import MenuItem
from .vote import Vote
from .feedback import Feedback

class Employee(User):
    def view_notifications(self):
        notifications = Notification.get_notifications("employee")
        for notification in notifications:
            print(notification['message'])

    def view_todays_menu(self):
        today_menu = MenuItem.get_todays_menu()
        for item in today_menu:
            print(f"Meal: {item['name']}, Price: {item['price']}")

    def vote(self):
        item_id = int(input("Enter meal ID to vote for: "))
        Vote.cast_vote(self.user_id, item_id)
        print("Vote casted.")

    def provide_feedback(self):
        item_id = int(input("Enter meal ID to provide feedback for: "))
        comment = input("Enter your comment: ")
        rating = int(input("Enter your rating (1-5): "))
        Feedback.add_feedback(self.user_id, item_id, comment, rating)
        print("Feedback submitted.")
