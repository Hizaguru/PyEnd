CREATE DATABASE [IF NOT EXISTS] image_gallery;

Use image_gallery;

CREATE TABLE IF NOT EXISTS Image (
    ID int NOT NULL AUTO_INCREMENT,
    Filename varchar(255) NOT NULL,
    Photo MEDIUMBLOB,
    Caption varchar(255),
    Size varchar(255),
    PRIMARY KEY (ID)
);