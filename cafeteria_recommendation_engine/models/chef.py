from .user import User
from .notification import Notification
# from .menu_item import MenuItem
from .vote import Vote
from .feedback import Feedback

class Chef(User):
    def view_notifications(self):
        notifications = Notification.get_notifications("chef")
        for notification in notifications:
            print(notification['message'])

    def view_algo_recommended(self):
        print("Displaying algorithmically recommended meals...")

    def rollout_option(self):
        print("Rolling out meal options for tomorrow...")
        Notification.create("New meal options available for voting", "employee")

    def publish_report(self):
        print("Publishing monthly report...")
        feedbacks = Feedback.get_monthly_feedback()
        for feedback in feedbacks:
            print(f"Meal: {feedback['item_id']}, Rating: {feedback['rating']}, Comment: {feedback['comment']}")

    def view_today_meal(self):
        votes = Vote.get_today_votes()
        for vote in votes:
            print(f"Meal: {vote['item_id']}, Votes: {vote['count']}")

    def view_ratings(self):
        ratings = Feedback.get_ratings()
        for rating in ratings:
            print(f"Meal: {rating['item_id']}, Rating: {rating['average_rating']}")
