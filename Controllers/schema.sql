DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS rank;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,  
  password TEXT NOT NULL,
  surname TEXT NOT NULL,
  name TEXT NOT NULL,
);

CREATE TABLE rank (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id)
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  score INTEGER NOT NULL  
);