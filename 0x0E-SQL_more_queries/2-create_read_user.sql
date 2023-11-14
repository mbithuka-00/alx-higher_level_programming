-- this creates the database hbtn_0d_2 and the user user_0d_2
-- and then creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- here it creates a user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- and then grants SELECT privileges to a user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;

