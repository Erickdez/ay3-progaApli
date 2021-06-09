CREATE TABLE `testdb`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `user_email` VARCHAR(50) NOT NULL,
  `password` VARCHAR(60) NOT NULL,
  `salt` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`));