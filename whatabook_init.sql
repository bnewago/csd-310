DROP USER IF EXISTS 'whatabook_user'@'localhost';


CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

    #all privileges granted to whatabook user.
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;


DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


   
   
   
    # creating tables for store, book, user, and wishlist.

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


INSERT INTO store(locale)
    VALUES('1234 Reindeer Way, Santas Home, Antartica 77741');

INSERT INTO book(book_name, author, details)
    VALUES('House of Sky and Breath', 'Sarah J. Maas', 'Choosing between staying silent or fighting');

INSERT INTO book(book_name, author, details)
    VALUES('Sierra Six', 'Mark Greaney', 'A ghost from the past');

INSERT INTO book(book_name, author, details)
    VALUES('It Ends With Us', 'Colleen Hoover', "Rekindling the flame from a past lover");

INSERT INTO book(book_name, author, details)
    VALUES('Diablo Mesa', 'Douglas Preston, Lincoln Child', "Cold Case Breakthrough");

INSERT INTO book(book_name, author, details)
    VALUES('Life Force', 'Tony Robbins', "Medicinal Advances");

INSERT INTO book(book_name, author, details)
    VALUES("Atomic Habits", 'James Clear', "Breaking bad habits and forming new ones");

INSERT INTO book(book_name, author, details)
    VALUES('Verity', 'Colleen Hoover', "Finishing works of an injured author");

INSERT INTO book(book_name, author, details)
    VALUES('Reminders of Him', 'Colleen Hoover', "Life after Prison");

INSERT INTO book(book_name, author, details)
    VALUES('James and the Giant Peach', 'Roald Dahl', "A journey to New York City");

    # adding the users in
INSERT INTO user(first_name, last_name) 
    VALUES('Jennifer', 'Lawrence');

INSERT INTO user(first_name, last_name)
    VALUES('Liam', 'Hemsworth');

INSERT INTO user(first_name, last_name)
    VALUES('Jeff', 'Gordon');


INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jennifer'), 
        (SELECT book_id FROM book WHERE book_name = 'James and the Giant Peach')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Liam'),
        (SELECT book_id FROM book WHERE book_name = 'Reminders of Him')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jeff'),
        (SELECT book_id FROM book WHERE book_name = 'Life Force')
    )

