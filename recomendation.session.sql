USE recomendation_db;




-- select * from detailedfeedback;

-- SELECT user, host, plugin FROM mysql.user WHERE user = 'admin';

-- SELECT CURRENT_USER();

-- select * from notification;
-- DELETE FROM notification 
-- WHERE notificationID BETWEEN 59 AND 60;


-- SELECT notificationID, message 
-- FROM Notification 
-- WHERE userID = 3 AND message
-- LIKE 'We are trying to improve your experience with%'


-- ALTER TABLE feedback
-- DROP FOREIGN KEY feedback_ibfk_2;

-- ALTER TABLE feedback
-- ADD CONSTRAINT feedback_ibfk_2 FOREIGN KEY (foodItemID) REFERENCES fooditem(foodItemID) ON DELETE CASCADE ON UPDATE CASCADE;



-- Step 2: Add the foreign key constraint to reference the 'category' column in the 'FoodItem' table

-- UPDATE recommendation  r
-- JOIN fooditem f ON r.fooditemID = f.foodItemID
-- SET r.category = f.category;


-- SELECT * FROM user;

-- select * from EmployeeProfile;
-- select * from votes;

-- select * from notification;

-- select itemName from fooditem where foodItemID = 59;

-- INSERT INTO Votes (userID, foodItemID, date)
-- VALUES (3, 34, DATE_SUB(CURRENT_TIMESTAMP, INTERVAL 1 DAY));


-- ALTER TABLE fooditem
-- ADD COLUMN category VARCHAR(50);


-- ALTER TABLE feedback
-- ADD COLUMN category VARCHAR(50);


-- UPDATE feedback f
-- JOIN fooditem fi ON f.foodItemID = fi.foodItemID
-- SET f.category = fi.category;


-- CREATE TRIGGER before_feedback_insert
-- BEFORE INSERT ON Feedback
-- FOR EACH ROW
-- BEGIN
--     DECLARE food_category VARCHAR(50);

--     -- Get the category from the FoodItem table
--     SELECT category INTO food_category
--     FROM FoodItem
--     WHERE foodItemID = NEW.foodItemID;

--     -- Set the category in the new Feedback record
--     SET NEW.category = food_category;
-- END;

-- UPDATE feedback SET category = 'Dinner' where category = '6'


-- CREATE TABLE FoodItemProfile (
--     foodItemID INT PRIMARY KEY,
--     dietPreference ENUM('Vegetarian', 'Non Vegetarian', 'Eggetarian'),
--     spiceLevel ENUM('High', 'Medium', 'Low'),
--     cuisinePreference ENUM('North Indian', 'South Indian', 'Other'),
--     sweetTooth ENUM('Yes', 'No'),
--     FOREIGN KEY (foodItemID) REFERENCES FoodItem(foodItemID)
-- );


-- INSERT INTO Votes ( userID, foodItemID, date)
-- VALUES (3, 40, '2024-07-16 00:00:00');
