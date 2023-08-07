/*
Assignment 12.3
August 3rd, 2023
Jeff Haberman
CYBR 410
SQL script to create whatabook database, tables, SQL user, and input records
*/

/*Drop the database*/
DROP DATABASE whatabook;

/*Drop the user for the database*/
DROP USER 'whatabook_user'@'localhost';

/*Create whatabook database*/
CREATE DATABASE whatabook;

/*Create SQL user for whatabook database*/
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

/*Granting full access to whatabook_user*/
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

/*Creating Tables*/
USE whatabook;
CREATE TABLE user(
    user_id     INT             NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
);
CREATE TABLE book(
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    author      VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE wishlist(
    wishlist_id     INT     NOT NULL    AUTO_INCREMENT,
    user_id         INT     NOT NULL,
    book_id         INT     NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user 
    FOREIGN KEY(user_id)
        REFERENCES user(user_id),
    CONSTRAINT fk_book
    FOREIGN KEY(book_id)
        REFERENCES book(book_id)
);

CREATE TABLE store(
    store_id    INT     NOT NULL,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

/*Inserting new books into book table*/
INSERT INTO book(book_name, details, author)
    VALUES ('Teach Yourself SQL',"Expert trainer and popular author Ben Forta teaches you just the parts of SQL you need to know-starting with simple data retrieval and quickly going on to more complex topics including the use of joins, subqueries, stored procedures, cursors, triggers, and table constraints.",'Ben Forta');

INSERT INTO book(book_name, details, author)
    VALUES ('Python Crash Course',"The best-selling Python book in the world, with over 1 million copies sold! A fast-paced, no-nonsense, updated guide to programming in Python.",'Eric Matthes');

INSERT INTO book(book_name, details, author)
    VALUES ('Basics of Digital Forensics',"This book offers guidance on how to conduct examinations by discussing what digital forensics is, the methodologies used, key tactical concepts, and the tools needed to perform examinations.", 'John Sammons');

INSERT INTO book(book_name, details, author)
    VALUES ('Kitchen Confidential',"A deliciously funny, delectably shocking banquet of wild-but-true tales of life in the culinary trade from Chef Anthony Bourdain",'Anthony Bourdain');

INSERT INTO book(book_name, details, author)
    VALUES ('Walden',"",'Henry David Thoreau');

INSERT INTO book(book_name, details, author)
    VALUES ('Gift From The Sea',"Drawing inspiration from the shells on the shore, Lindbergh's musings on the shape of a woman's life will bring new understanding to readers, male, female, and family, at any stage of life.",'Anne Morrow Lindbergh');

INSERT INTO book(book_name, details, author)
    VALUES ('The Body Keeps The Score',"",'Bessel Van Der Kolk');

INSERT INTO book(book_name, details, author)
    VALUES ('Surprise, Kill, Vanish',"Brings to vivid life the sheer pandemonium and chaos, as well as the unforgettable human will to survive and the intellectual challenge of not giving up hope that define paramilitary and intelligence work",'Annie Jacobsen');

INSERT INTO book(book_name, details, author)
    VALUES ('Untamed',"",'Glennon Doyle');

/*Inserting new users into user table*/
INSERT INTO user(first_name, last_name)
    VALUES ('Jeff','Haberman');

INSERT INTO user(first_name, last_name)
    VALUES ('John','Smith');

INSERT INTO user(first_name, last_name)
    VALUES ('Betty','White');

/*Inserting wish lists into wishlist table*/
INSERT INTO wishlist(user_id,book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jeff'),
        (SELECT book_id FROM book WHERE book_name = 'Surprise, Kill, Vanish')
    );

INSERT INTO wishlist(user_id,book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'),
        (SELECT book_id FROM book WHERE book_name = 'Kitchen Confidential')
    );

INSERT INTO wishlist(user_id,book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Betty'),
        (SELECT book_id FROM book WHERE book_name = 'Gift from the Sea')
    );

/*Inserting a new store*/
INSERT INTO store(store_id,locale)
    VALUES (
        1,'123 Main Street, Bellevue, Nebraska, 68005'
    );