create TABLE Practise (
    notificationid INT AUTO_INCREMENT PRIMARY key,
    userID INT 
    foreign key (userID) refe
)

create TRIGGER before_delete_user
BEFORE DELETE on user
for each row