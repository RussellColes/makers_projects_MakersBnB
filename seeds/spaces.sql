-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    location VARCHAR(255),
    description VARCHAR(255),
    price_per_night int,
    user_id int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (title, location, description, price_per_night, user_id) VALUES ('Title 1', 'Location 1', 'Description 1', 10, 1);
INSERT INTO spaces (title, location, description, price_per_night, user_id) VALUES ('Title 2', 'Location 2', 'Description 2', 20, 2);
INSERT INTO spaces (title, location, description, price_per_night, user_id) VALUES ('Title 3', 'Location 3', 'Description 3', 30, 3);
