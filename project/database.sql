CREATE DATABASE [IF NOT EXISTS] Image_gallery;

Use Image_gallery;

CREATE TABLE IF NOT EXISTS Image (
    ID int NOT NULL AUTO_INCREMENT,
    Caption varchar(255) NOT NULL,
    Filename varchar(255),
    Size varchar(255),
    PRIMARY KEY (ID)
);