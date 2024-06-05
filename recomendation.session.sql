CREATE TABLE Users (
    userID INT PRIMARY KEY,
    name VARCHAR(100),
    role ENUM('Admin', 'Chef', 'Employee'),
    password VARCHAR(100)
);


CREATE TABLE Menu (
    menuID INT PRIMARY KEY,
    date DATE
);

CREATE TABLE FoodItem (
    foodItemID INT PRIMARY KEY,
    itemName VARCHAR(100),
    price DECIMAL(10, 2),
    availability BOOLEAN,
    menuID INT,
    FOREIGN KEY (menuID) REFERENCES Menu(menuID)
);
