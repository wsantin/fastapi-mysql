DROP DATABASE demo;
CREATE DATABASE demo;

CREATE TABLE users(
    id INTEGER auto_increment not null,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    description VARCHAR(150),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	disabled_at DATETIME,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;