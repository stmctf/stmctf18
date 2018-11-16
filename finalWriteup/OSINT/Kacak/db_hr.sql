-- MySQL dump 10.16  Distrib 10.1.29-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ctf
-- ------------------------------------------------------
-- Server version	10.1.29-MariaDB-6

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bilgi`
--

DROP TABLE IF EXISTS `bilgi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bilgi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ad` varchar(20) DEFAULT NULL,
  `soyad` varchar(30) DEFAULT NULL,
  `dogum_yeri` varchar(30) DEFAULT NULL,
  `dogum_yili` varchar(30) DEFAULT NULL,
  `ikametgah` varchar(30) DEFAULT NULL,
  `sosyal_medya_hesabi` varchar(30) DEFAULT NULL,
  `ehliyet` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bilgi`
--

LOCK TABLES `bilgi` WRITE;
/*!40000 ALTER TABLE `bilgi` DISABLE KEYS */;
INSERT INTO `bilgi` VALUES (1,'Mehmet','Yilmaz','Trabzon','1986','Ankara','mhmt_ylmz','B'),(2,'Can','Kaya','Istanbul','1995','Ankara','Yok','A,B'),(3,'Tugce','Kaya','Izmir','1990','Izmır','tugcek_','B'),(4,'Erdinc','Kaya','Antalya','1988','Ankara','erdinckaya','Yok'),(5,'Ege','Deniz','Mugla','1991','Ankara','halikarnasli48','B'),(6,'Ertan','Yilmaz','Elazig','1992','Ankara','mhmt_ylmz','B'),(7,'Nesrin','Koca','Afyon','1985','Ankara','nsrnkoca85','B'),(8,'Muge','Ok','Denizli','1989','Ankara','mugeok06','B'),(9,'Erhan','Ali','Konya','1976','Edirne','crazyboy76','B'),(10,'Aykut','Kaya','Aydin','1980','Eskisehir','aykutkaya','B'),(11,'Hulya','Artı','Ankara','1982','Ankara','hulyarti2000','B'),(12,'Merve','Rizeli','Rize','1984','Ankara','Yok','Yok');
/*!40000 ALTER TABLE `bilgi` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-20 19:58:18
