-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: bdvacunatorio
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `laboratorio_vacuna`
--

DROP TABLE IF EXISTS `laboratorio_vacuna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `laboratorio_vacuna` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_laboratorio` int NOT NULL,
  `id_vacuna` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laboratorio_vacuna`
--

LOCK TABLES `laboratorio_vacuna` WRITE;
/*!40000 ALTER TABLE `laboratorio_vacuna` DISABLE KEYS */;
INSERT INTO `laboratorio_vacuna` VALUES (117,37,6),(118,34,9),(119,35,9),(120,36,9),(129,34,5);
/*!40000 ALTER TABLE `laboratorio_vacuna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `laboratorios`
--

DROP TABLE IF EXISTS `laboratorios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `laboratorios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laboratorios`
--

LOCK TABLES `laboratorios` WRITE;
/*!40000 ALTER TABLE `laboratorios` DISABLE KEYS */;
INSERT INTO `laboratorios` VALUES (34,'ASTRAZENECA'),(35,'SPUTNIK'),(36,'SINOPHARM'),(37,'RICHMOND');
/*!40000 ALTER TABLE `laboratorios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `turnos`
--

DROP TABLE IF EXISTS `turnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turnos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `fecha_solicitud` date DEFAULT NULL,
  `fecha_turno` date DEFAULT NULL,
  `sede` varchar(50) DEFAULT NULL,
  `vacuna` varchar(50) NOT NULL,
  `numero_dosis` int DEFAULT NULL,
  `estado` int NOT NULL,
  `notificado` tinyint DEFAULT NULL,
  `asistio` tinyint DEFAULT NULL,
  `laboratorio` varchar(50) DEFAULT NULL,
  `lote` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=227 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turnos`
--

LOCK TABLES `turnos` WRITE;
/*!40000 ALTER TABLE `turnos` DISABLE KEYS */;
INSERT INTO `turnos` VALUES (181,163,'2022-06-15','2022-06-22','Municipal','Covid',1,2,0,1,'SINOPHARM','988'),(182,163,'2022-06-22','2022-06-29','Municipal','Gripe',0,2,0,1,'RICHMOND','6555'),(183,164,'2022-06-15','2022-06-22','Cementerio','Covid',1,2,0,1,'SPUTNIK','232111'),(184,164,'2022-06-15','2022-06-29','Cementerio','Gripe',0,2,0,1,'RICHMOND','12222'),(185,165,'2022-06-15','2022-06-22','Terminal','Covid',1,2,0,1,'SINOPHARM','99888'),(186,165,'2022-06-22','2022-06-29','Terminal','Gripe',0,2,0,1,'RICHMOND','98887'),(187,164,'2022-06-29','2022-07-20','Cementerio','Covid',2,0,1,0,'',''),(188,163,'2022-06-29','2022-07-20','Municipal','Covid',2,0,0,0,'',''),(189,165,'2022-06-29','2022-07-28','Terminal','Covid',2,0,0,0,'',''),(190,155,'2022-06-22','2022-06-29','Municipal','Gripe',1,2,0,1,'RICHMOND','122111'),(191,155,'2022-05-10','2022-06-22','Municipal','Covid',1,2,0,1,'SINOPHARM','3322'),(193,156,'2022-06-22','2022-06-29','Terminal','Gripe',1,2,0,1,'RICHMOND','99999'),(194,157,'2022-06-22','2022-06-29','Cementerio','Covid',1,2,0,1,'SINOPHARM','6544'),(195,157,'2022-06-29','2022-08-03','Cementerio','Covid',2,0,0,0,'ASTRAZENECA','25235'),(196,158,'2022-06-22','2022-06-22','Municipal','Covid',1,0,0,0,'',''),(197,158,'2022-06-22','2022-06-29','Municipal','Gripe',1,2,0,1,'RICHMOND','2222'),(199,159,'2022-06-22','2022-06-29','Municipal','Gripe',1,2,0,1,'RICHMOND','112233'),(200,159,'2022-06-29','2022-07-06','Municipal','Covid',1,0,0,0,'',''),(201,160,'2022-06-22','2022-06-29','Terminal','Gripe',1,2,0,1,'RICHMOND','18889'),(202,160,'2022-06-29','2023-07-07','Terminal','Gripe',1,0,0,0,'',''),(203,160,'2022-06-29','2022-07-08','Terminal','Covid',1,0,0,0,'',''),(204,161,'2022-06-22','2022-06-29','Terminal','Covid',1,2,0,1,'SPUTNIK','1111112222'),(205,161,'2022-06-29','2022-07-03','Terminal','Gripe',1,2,0,1,'RICHMOND','2222'),(206,162,'2022-06-29','2022-07-06','Terminal','Covid',1,0,0,0,'',''),(207,162,'2022-06-29','2022-07-26','Terminal','Gripe',1,0,0,0,'',''),(208,162,'2022-06-29','2022-08-08','Terminal','Covid',2,0,0,0,'',''),(209,161,'2022-06-29','2022-07-20','Terminal','Covid',2,0,0,0,'',''),(210,166,'2020-06-30','2020-06-30','Terminal','Gripe',1,2,0,1,'RICHMOND','22311'),(211,166,'2022-06-20','2022-07-05','Terminal','Covid',1,0,0,0,'',''),(214,167,'2022-06-20','2022-07-05','Terminal','Gripe',1,0,0,0,'',''),(215,168,'2022-06-28','2022-07-05','Municipal','Covid',1,0,0,0,'',''),(216,169,'2022-06-25','2022-07-05','Municipal','Covid',2,0,0,0,'',''),(217,170,'2022-06-26','2022-07-05','Municipal','Covid',1,0,0,0,'',''),(218,171,'2022-06-27','2022-07-05','Cementerio','Gripe',1,0,1,0,'',''),(219,172,'2022-06-28','2022-07-05','Cementerio','Covid',1,0,0,0,'',''),(220,173,'2022-06-30','2022-07-07','Cementerio','Covid',1,0,0,0,'',''),(221,174,'2022-06-30','2022-06-30','Cementerio','Covid',1,2,0,1,'SINOPHARM','2213211'),(222,174,'2022-06-30','2022-07-21','Cementerio','Covid',2,0,1,0,'',''),(223,175,'2019-07-01','2019-07-09','Cementerio','Gripe',1,2,0,1,'RICHMOND','2223'),(224,176,'2020-07-01','2020-07-09','Terminal','Gripe',1,2,0,1,'RICHMOND','66655'),(226,178,'2021-07-01','2021-07-09','Terminal','Gripe',1,2,0,1,'RICHMOND','121212');
/*!40000 ALTER TABLE `turnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(100) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `telefono` varchar(100) DEFAULT NULL,
  `nacimiento` date DEFAULT NULL,
  `primera_dosis` tinyint(1) DEFAULT NULL,
  `fecha_primera_dosis` date DEFAULT NULL,
  `fecha_ultima_gripe` date DEFAULT NULL,
  `fecha_ultima_covid` date DEFAULT NULL,
  `paciente_riesgo` tinyint(1) DEFAULT NULL,
  `fiebre_amarilla` tinyint(1) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `dni` varchar(100) DEFAULT NULL,
  `sede_preferida` varchar(100) DEFAULT NULL,
  `sede` varchar(100) DEFAULT NULL,
  `tipo` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (56,'admin','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'admin',NULL,'12345678',NULL,NULL,1),(90,NULL,'Pedro','Gonzalez','22132111',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3211','pedro@gmail.com','22222221',NULL,'Terminal',2),(145,NULL,'Adolfo','Pedernera','2216565',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3211','adolfo@gmail.com','22222222',NULL,'Municipal',2),(146,NULL,'Homar','Sivori','22132111',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3211','homar@hotmail.com','22222223',NULL,'Terminal',2),(155,NULL,'Diego','Molina','2216544','2014-05-20',0,'2022-06-29','2022-06-29','2022-06-29',0,0,'3211','diego@gmail.com','11111111','Municipal','0',3),(156,NULL,'Leonardo','Astrada','22132111','2010-06-11',0,NULL,'2022-06-29',NULL,0,0,'3211','leonardo@gmail.com','11111112','Terminal','0',3),(157,NULL,'Federico','Pipo','22132111','2011-03-11',0,'2022-06-29',NULL,'2022-07-03',0,0,'3211','federico@gmail.com','11111113','Municipal','0',3),(158,NULL,'Diego','Barrado','22165444','1995-06-11',0,NULL,'2022-06-29',NULL,0,0,'3211','diegobarrado@gmail.com','11111114','Cementerio','0',3),(159,NULL,'Pablo','Fermin','22132222','1999-05-20',0,NULL,NULL,NULL,0,1,'3211','pablin@gmail.com','11111115','Municipal','0',3),(160,NULL,'Mauricio','Mauri','2246544','1985-01-30',0,NULL,NULL,NULL,0,1,'3211','mauri@gmail.com','11111116','Cementerio','0',3),(161,NULL,'Chavo','Bianca','2213211','1997-05-11',0,'2022-06-29',NULL,NULL,0,1,'3211','chavo@gmail.com','11111117','Terminal','0',3),(162,NULL,'Pipo','Gorosito','6544444','1994-05-23',0,NULL,NULL,NULL,0,0,'3211','pipo@gmail.com','11111118','Terminal','0',3),(163,NULL,'Ernesto','Salomón','2213211','1940-10-10',0,'2022-06-29','2022-06-29',NULL,0,0,'3211','ernesti@gmail.com','11111119','Municipal','0',3),(164,NULL,'Anastacia','Luisa','65445465','1934-11-15',0,'2022-06-29','2022-06-29',NULL,0,0,'3211','anastacia@hotmail.com','11111110','Cementerio','0',3),(165,NULL,'Joaquin','Pineda','2232111','1933-06-11',0,'2022-06-29','2022-06-29',NULL,0,0,'3211','joaquin@gmail.com','11111120','Terminal','0',3),(166,NULL,'Oscar','Rodriguez','221123211','1998-06-20',0,NULL,'2020-06-30',NULL,0,0,'3211','oscar@gmail.com','33333333','Municipal','0',3),(167,NULL,'Pablo','Perico','111321121','2001-12-20',0,NULL,NULL,NULL,0,0,'3211','pperico@gmail.com','33333334','Terminal','0',3),(168,NULL,'Luis','Amuchastegui','221321111','1999-04-03',0,NULL,NULL,NULL,0,0,'3211','luigi@gmail.com','33333335','Municipal','0',3),(169,NULL,'Mario','Mordini','22132111','1980-08-16',0,'2021-01-20',NULL,NULL,0,0,'3211','marito@gmail.com','33333336','Municipal','0',3),(170,NULL,'Juan','Andrés','22132111','1990-03-14',0,NULL,NULL,NULL,0,0,'3211','juancho@gmail.com','33333337','Municipal','0',3),(171,NULL,'Luciano','Trecarichi Rios','22132111','1986-11-19',1,NULL,NULL,NULL,0,0,'3211','lucianotrecarichi@gmail.com','32783653','Cementerio','0',3),(172,NULL,'Juan','Fernando','22132111','1979-01-11',0,NULL,NULL,NULL,0,0,'3211','sdlbsso@gmail.com','33333339','Cementerio','0',3),(173,NULL,'Juana','Fernanda','221321111','1991-06-12',0,NULL,NULL,NULL,0,0,'3211','juanita@gmail.com','44444444','Cementerio','0',3),(174,NULL,'Felipe','Melo','22132111','1992-06-20',0,'2022-06-30',NULL,NULL,0,0,'3211','felipao@gmail.com','55555555','Cementerio','0',3),(175,NULL,'Mauro','Pelegrino','22132111','2001-05-11',0,NULL,'2019-07-09',NULL,0,0,'3211','miau@gmail.com','66666666','Municipal','0',3),(176,NULL,'Patricia','Rodriguez','22132111','1999-02-20',0,NULL,'2020-07-09',NULL,0,0,'3211','pato@gmail.com','77777777','Terminal','0',3),(177,NULL,'Nadia ','Aguirre','22132111','1980-02-20',0,NULL,NULL,NULL,0,0,'3211','nadia@gmail.com','88888888','Cementerio','0',3),(178,NULL,'Facundo','Pérez','2113211','1985-05-20',0,NULL,'2021-07-09',NULL,0,0,'3211','facund@gmail.com','99999999','Terminal','0',3),(179,NULL,'Ana ','Sosa','32265265','2003-01-03',0,NULL,NULL,NULL,0,0,'3211','sdfsdf@gmail.com','20000000','Cementerio','0',3),(180,NULL,'Analia','Ramos','3115155151','1995-10-03',0,NULL,NULL,NULL,0,0,'3211','sadasfsaf@gmail.com','20000001','Cementerio','0',3);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacunas`
--

DROP TABLE IF EXISTS `vacunas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacunas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacunas`
--

LOCK TABLES `vacunas` WRITE;
/*!40000 ALTER TABLE `vacunas` DISABLE KEYS */;
INSERT INTO `vacunas` VALUES (5,'Gripe'),(6,'Fiebre amarilla'),(9,'Covid');
/*!40000 ALTER TABLE `vacunas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-04 10:05:56
