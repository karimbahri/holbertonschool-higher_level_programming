-- create_user

-- create user with all privileges
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY "user_0d_1_pwd";
-- grant all privilegs
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
