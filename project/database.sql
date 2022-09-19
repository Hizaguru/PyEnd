CREATE DATABASE image_gallery;

Use image_gallery;

CREATE TABLE IF NOT EXISTS Image (
    ID int NOT NULL AUTO_INCREMENT,
    Filename varchar(255) NOT NULL,
    Photo MEDIUMBLOB,
    Caption varchar(255),
    Size varchar(255),
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS `accounts` (
	`ID` int(11) NOT NULL AUTO_INCREMENT,
  	`Username` varchar(50) NOT NULL,
  	`Password` varchar(255) NOT NULL,
  	`Email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `accounts` (`Id`, `Username`, `Password`, `Email`) VALUES (1, 'test', 'test', 'test@test.com');