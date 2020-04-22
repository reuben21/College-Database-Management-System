CREATE DATABASE  IF NOT EXISTS `studentdbms` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `studentdbms`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: studentdbms
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `administrator`
--

DROP TABLE IF EXISTS `administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator` (
  `Admin_Username` varchar(50) NOT NULL,
  `Admin_Password` varchar(45) NOT NULL,
  `admin_phone_no` bigint NOT NULL,
  `admin_email_id` varchar(45) NOT NULL,
  `Admin_FullName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Admin_Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator`
--

LOCK TABLES `administrator` WRITE;
/*!40000 ALTER TABLE `administrator` DISABLE KEYS */;
INSERT INTO `administrator` VALUES ('admin','admin',7894565555,'normasd@gmail.com','Admin Admin'),('Reuben','Reuben',7231745864,'reuben211999@gmail.com','Reuben Coutinho');
/*!40000 ALTER TABLE `administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `course_id` varchar(45) NOT NULL,
  `course_name` varchar(45) DEFAULT NULL,
  `dept_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`course_id`),
  KEY `fk_course_department1_idx` (`dept_id`),
  CONSTRAINT `fk_course_department1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES ('AAAAAA','AAAAAAAAAAAAAAAAAAAAAAAAAAA',NULL),('ITC401','Applied Mathematics-IV','INFT'),('ITC402','Computer Networks','INFT'),('ITC403','Operating Systems','INFT'),('ITC404','Computer Organization and Architecture','INFT'),('ITC405','Automata Theory','INFT'),('ITL401','Networking Lab','INFT'),('ITL402','Unix Lab','INFT'),('ITL403','Microprocessor\nProgramming Lab','INFT'),('ITL404','Python Lab','INFT');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `dept_id` varchar(45) NOT NULL,
  `DepartmentName` varchar(45) DEFAULT NULL,
  `hod` varchar(45) NOT NULL,
  `budget` decimal(15,0) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('AAAAAAA','AAAAAAAAAA','AAAAAAAAAA',250000),('CMPN','COMPUTER ENGINEERING','Dr.Terry Jeffords',2000000),('ELEC','ELECTRONICS ENGINEERING','Dr.Charles Boyle',2000000),('EXTC','ELECTRONICS AND TELECOMMUNICATION ENGINEERING','Dr.Jacob Peralta',1000000),('INFT','INFORMATION TECHNOLOGY','Dr. Amy Santiago',2000000),('MECH','MECHANICAL ENGINEERING','Dr.Raymod Holt',9000000);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_scheme`
--

DROP TABLE IF EXISTS `exam_scheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_scheme` (
  `ExamIDs` int NOT NULL AUTO_INCREMENT,
  `PID` int NOT NULL,
  `course_id` varchar(45) NOT NULL,
  `IAT_1` decimal(8,3) DEFAULT '0.000',
  `IAT_2` decimal(8,3) DEFAULT '0.000',
  `IAT_AVG` decimal(8,3) DEFAULT '0.000',
  `AT_1` decimal(8,3) DEFAULT '0.000',
  `AT_2` decimal(8,3) DEFAULT '0.000',
  `AT_AVG` decimal(8,3) DEFAULT '0.000',
  PRIMARY KEY (`ExamIDs`),
  KEY `course_id_idx` (`course_id`),
  KEY `fk_Exam_Scheme_student_registration1_idx` (`PID`),
  CONSTRAINT `course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  CONSTRAINT `fk_Exam_Scheme_student_registration1` FOREIGN KEY (`PID`) REFERENCES `student_registration` (`PID`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_scheme`
--

LOCK TABLES `exam_scheme` WRITE;
/*!40000 ALTER TABLE `exam_scheme` DISABLE KEYS */;
INSERT INTO `exam_scheme` VALUES (36,181035,'ITC401',15.000,14.500,16.125,7.000,7.000,7.500),(37,181035,'ITC402',18.000,17.000,16.333,6.000,7.000,6.333),(38,181035,'ITC403',13.000,17.000,14.250,5.500,7.000,7.250),(39,181035,'ITC404',20.000,15.000,18.250,7.000,8.000,8.000),(40,181035,'ITC405',16.000,12.000,14.000,6.500,8.000,7.125),(45,181036,'ITC401',0.000,0.000,0.000,0.000,0.000,0.000),(46,181036,'ITC402',NULL,NULL,NULL,NULL,NULL,NULL),(47,181036,'ITC403',NULL,NULL,NULL,NULL,NULL,NULL),(48,181036,'ITC404',NULL,NULL,NULL,NULL,NULL,NULL),(49,181036,'ITC405',NULL,NULL,NULL,NULL,NULL,NULL),(50,181036,'ITL401',NULL,NULL,NULL,NULL,NULL,NULL),(51,181036,'ITL402',NULL,NULL,NULL,NULL,NULL,NULL),(52,181036,'ITL403',NULL,NULL,NULL,NULL,NULL,NULL),(53,181036,'ITL404',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `exam_scheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty` (
  `fac_id` int NOT NULL AUTO_INCREMENT,
  `passwd` varchar(45) NOT NULL,
  `dept_id` varchar(45) NOT NULL,
  `qualification` varchar(45) NOT NULL,
  `birthdate` date NOT NULL,
  `full_Name` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `phone_no` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `email_id` varchar(45) DEFAULT NULL,
  `experience` varchar(45) DEFAULT NULL,
  `login_date_time` datetime(6) DEFAULT NULL,
  `login_ip` varchar(45) DEFAULT NULL,
  `profile_picture` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`fac_id`),
  KEY `dept_id_idx` (`dept_id`),
  CONSTRAINT `dept_id` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=210034 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` VALUES (210030,'1234','INFT','Master of Engineering ','1986-04-25','Denizl Dsouza','North East state','7894561231','Male','Normay@gmail.com','More Than 5 Years','2020-04-18 14:45:55.000000','45.250.46.81','https://image-bucket21.s3.ap-south-1.amazonaws.com/210030.png'),(210032,'1234','INFT','Bachelor of Engineering ','1981-05-06','Suderland roy','45,Roy Street','7894561237','Female','normaay52@gmail.com','3 Years','2020-04-19 00:36:59.000000','45.250.46.81','https://image-bucket21.s3.ap-south-1.amazonaws.com/210032.png'),(210033,'1234','INFT','Master of Engineering ','1981-05-06','lander roy','45,Roy Street','7894111111','Male','normaay52@gmail.com','More Than 5 Years','2020-04-19 00:37:40.000000','45.250.46.81','https://image-bucket21.s3.ap-south-1.amazonaws.com/210033.png');
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `feedbackid` int NOT NULL AUTO_INCREMENT,
  `course_id` varchar(45) DEFAULT NULL,
  `explainantion` int DEFAULT NULL,
  `Punctuality` int DEFAULT NULL,
  `Class_Handling` int DEFAULT NULL,
  `Comments` mediumtext,
  PRIMARY KEY (`feedbackid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,NULL,NULL,NULL,NULL,NULL),(2,NULL,NULL,NULL,NULL,NULL),(3,NULL,NULL,NULL,NULL,NULL),(4,NULL,NULL,NULL,NULL,NULL),(5,NULL,NULL,NULL,NULL,NULL),(6,NULL,NULL,NULL,NULL,NULL),(7,'ITC403',8,7,4,'14141'),(8,'ITC404',9,8,9,'142141'),(9,'ITC404',7,9,7,'Okay Okay');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `onetime`
--

DROP TABLE IF EXISTS `onetime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `onetime` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numbers` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `onetime`
--

LOCK TABLES `onetime` WRITE;
/*!40000 ALTER TABLE `onetime` DISABLE KEYS */;
/*!40000 ALTER TABLE `onetime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_registration`
--

DROP TABLE IF EXISTS `student_registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_registration` (
  `PID` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(45) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone_no` bigint DEFAULT NULL,
  `birthdate` date NOT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `passwd` varchar(45) NOT NULL,
  `email_id` varchar(100) NOT NULL,
  `id_dept` varchar(45) NOT NULL,
  `last_login_time_date` datetime DEFAULT NULL,
  `Approval` varchar(45) DEFAULT NULL,
  `profile_picture` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`PID`),
  KEY `class_id_idx` (`id_dept`),
  CONSTRAINT `fk_student_registration_Department1` FOREIGN KEY (`id_dept`) REFERENCES `department` (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=181037 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_registration`
--

LOCK TABLES `student_registration` WRITE;
/*!40000 ALTER TABLE `student_registration` DISABLE KEYS */;
INSERT INTO `student_registration` VALUES (181035,'Bart Henry','North State',7123456789,'2000-08-01','Male','1234','1234@gmail.com','INFT','2020-04-18 14:46:54','APPROVED','https://image-bucket21.s3.ap-south-1.amazonaws.com/181035.png'),(181036,'John Diaz','43,John street',7531594568,'1973-03-08','Male','1234','normaay52@gmail.com','INFT','2020-04-19 10:24:12','APPROVED','https://image-bucket21.s3.ap-south-1.amazonaws.com/181036.jpg');
/*!40000 ALTER TABLE `student_registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `takes`
--

DROP TABLE IF EXISTS `takes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `takes` (
  `TakesID` int NOT NULL AUTO_INCREMENT,
  `PID` int NOT NULL,
  `course_id` varchar(45) NOT NULL,
  `year` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`TakesID`),
  KEY `fk_Takes_Course1_idx` (`course_id`),
  KEY `fk_Takes_student_registration1_idx` (`PID`),
  CONSTRAINT `fk_takes_course1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  CONSTRAINT `fk_Takes_student_registration1` FOREIGN KEY (`PID`) REFERENCES `student_registration` (`PID`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `takes`
--

LOCK TABLES `takes` WRITE;
/*!40000 ALTER TABLE `takes` DISABLE KEYS */;
INSERT INTO `takes` VALUES (47,181035,'ITC401',NULL),(48,181035,'ITC402',NULL),(49,181035,'ITC403',NULL),(50,181035,'ITC404',NULL),(51,181035,'ITC405',NULL),(58,181036,'ITC401',NULL),(59,181036,'ITC402',NULL),(60,181036,'ITC403',NULL),(61,181036,'ITC404',NULL),(62,181036,'ITC405',NULL),(63,181036,'ITL401',NULL),(64,181036,'ITL402',NULL),(65,181036,'ITL403',NULL),(66,181036,'ITL404',NULL);
/*!40000 ALTER TABLE `takes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teaches`
--

DROP TABLE IF EXISTS `teaches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teaches` (
  `teacid` int NOT NULL AUTO_INCREMENT,
  `fac_id` int NOT NULL,
  `course_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`teacid`),
  KEY `fk_Teaches_Course1_idx` (`course_id`),
  KEY `fk_Teaches_faculty1_idx` (`fac_id`),
  CONSTRAINT `fk_Teaches_Course1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  CONSTRAINT `fk_teaches_faculty1` FOREIGN KEY (`fac_id`) REFERENCES `faculty` (`fac_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teaches`
--

LOCK TABLES `teaches` WRITE;
/*!40000 ALTER TABLE `teaches` DISABLE KEYS */;
INSERT INTO `teaches` VALUES (7,210030,'ITC402'),(8,210030,'ITL401'),(9,210032,'ITC405'),(10,210033,'ITC404'),(11,210030,'ITC401');
/*!40000 ALTER TABLE `teaches` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-19 16:21:48
