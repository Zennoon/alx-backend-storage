-- Creates a 'users' table with columns id, email, name, and country
-- Only creates the table if not already created (doesn't fail if
-- table already exists)
CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY AUTO_INCREMENT,
       	     	    	   	 email VARCHAR(255) UNIQUE NOT NULL,
		   		 name VARCHAR(255),
		   		 country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US')
