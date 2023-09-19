-- 3. MySQL setup development
/*
A database hbnb_dev_db
A new user hbnb_dev (in localhost)
The password of hbnb_dev should be set to hbnb_dev_pwd
hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail
*/

CREATE DATABASE IF NOT EXISTS hbnb_test_db;


USE hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test '@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT USAGE ON *.* TO 'hbnb_test '@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test '@'localhost';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test '@'localhost';


FLUSH PRIVILEGES;