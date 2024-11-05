DROP TABLE IF EXISTS availabilities;
DROP TABLE IF EXISTS bookings;
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
    headline_description VARCHAR(255),
    description VARCHAR(255),
    price_per_night int,
    user_id int,
    constraint fk_user foreign key(user_id) -- new code here!
    references users(id)
    on delete cascade
);

INSERT INTO spaces (title, location, headline_description, description, price_per_night, user_id) VALUES ('Title 1', 'Location 1', 'Headline description 1', 'Description 1', 10, 1);
INSERT INTO spaces (title, location, headline_description, description, price_per_night, user_id) VALUES ('Title 2', 'Location 2', 'Headline description 2', 'Description 2', 20, 2);
INSERT INTO spaces (title, location, headline_description, description, price_per_night, user_id) VALUES ('Title 3', 'Location 3', 'Headline description 3', 'Description 3', 30, 1);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    start_date DATE,
    end_date DATE,
    status VARCHAR(255),
    total_price int,
    space_id int,
    user_id int,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);   

INSERT INTO bookings (start_date, end_date, status, total_price, space_id, user_id) VALUES ('2024-11-10', '2024-11-13', 'confirmed', 30, 1, 1);
INSERT INTO bookings (start_date, end_date, status, total_price, space_id, user_id) VALUES ('2024-11-14', '2024-11-18', 'confirmed', 80, 2, 2);
INSERT INTO bookings (start_date, end_date, status, total_price, space_id, user_id) VALUES ('2024-11-15', '2024-11-16', 'pending', 60, 3, 1);

CREATE TABLE availabilities (
    id SERIAL PRIMARY KEY,
    space_id int,
    date DATE,
    is_available boolean,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade
);
    
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-10', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-11', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-12', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-13', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-14', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-15', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-16', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-17', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-18', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-10', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-11', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-12', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-13', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-14', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-15', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-16', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-17', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-18', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-10', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-11', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-12', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-13', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-14', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-15', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-16', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-17', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-18', True); 
