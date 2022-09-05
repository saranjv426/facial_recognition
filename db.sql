/*
SQLyog Community Edition- MySQL GUI v6.07
Host - 5.5.30 : Database - face_mask_detection
*********************************************************************
Server version : 5.5.30
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

create database if not exists `face_mask_detection`;

USE `face_mask_detection`;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*Table structure for table `personinfo` */

DROP TABLE IF EXISTS `personinfo`;

CREATE TABLE `personinfo` (
  `sno` varchar(500) DEFAULT NULL,
  `name` varchar(500) DEFAULT NULL,
  `age` varchar(500) DEFAULT NULL,
  `gender` varchar(500) DEFAULT NULL,
  `adrs` varchar(500) DEFAULT NULL,
  `picture` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `personinfo` */

insert  into `personinfo`(`sno`,`name`,`age`,`gender`,`adrs`,`picture`) values ('Arjun_5656','Arjun','34','Male','HYD','Arjun.jpg'),('Salman_5916','Salman','45','Male','Mumbai','Salman.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
