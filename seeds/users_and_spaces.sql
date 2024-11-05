DROP TABLE IF EXISTS spaces;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO users (name, email, password) VALUES ('Ben Cole', 'ben@example.com', 'password');
INSERT INTO users (name, email, password) VALUES ('Reena Sewraz', 'reena@example.com', 'password!');


CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    location VARCHAR(255),
    description VARCHAR(255),
    price_per_night int,
    user_id int,
    constraint fk_user foreign key(user_id) -- new code here!
    references users(id)
    on delete cascade
);

INSERT INTO spaces (title, location, description, price_per_night, user_id) VALUES ('Title 1', 'Location 1', 'Description 1', 10, 1);
INSERT INTO spaces (title, location, description, price_per_night, user_id) VALUES ('Title 2', 'Location 2', 'Description 2', 20, 2);
INSERT INTO spaces (title, location, description, price_per_night, user_id) VALUES ('Title 3', 'Location 3', 'Description 3', 30, 1);
