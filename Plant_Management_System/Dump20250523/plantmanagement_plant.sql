-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: plantmanagement
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `plant`
--

DROP TABLE IF EXISTS `plant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plant` (
  `id` int NOT NULL AUTO_INCREMENT,
  `plant_name` varchar(100) DEFAULT NULL,
  `plant_type` varchar(50) DEFAULT NULL,
  `tools_and_materials` longtext,
  `plants_component` longtext,
  `procedure` longtext,
  `user_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_plant_user_id` (`user_id`),
  CONSTRAINT `fk_plant_user_id` FOREIGN KEY (`user_id`) REFERENCES `userlist` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plant`
--

LOCK TABLES `plant` WRITE;
/*!40000 ALTER TABLE `plant` DISABLE KEYS */;
INSERT INTO `plant` VALUES (1,'Snake Plant (Sansevieria)','Succulent','Well-draining potting mix\r\n\r\nTerracotta pot with drainage\r\n\r\nGardening gloves\r\n\r\nPruning shears\r\n\r\nWatering can','Thick, upright leaves (variegated green and yellow)\r\n\r\nRhizome root system\r\n\r\nTough, waxy leaf surface','1. Choose a pot 1-2 inches wider than the root ball\r\n2. Fill pot 1/3 with potting mix\r\n3. Place plant in center and fill remaining space\r\n4. Water lightly after planting (only when soil is dry)\r\n5. Place in bright, indirect light\r\n6. Water every 2-3 weeks (less in winter)',3),(2,'Peace Lily (Spathiphyllum)','Tropical flowering plant','Peat-based potting mix\r\n\r\nPlastic pot with drainage\r\n\r\nMist spray bottle\r\n\r\nLiquid houseplant fertilizer','Glossy dark green leaves\r\n\r\nWhite flower spathes\r\n\r\nDense root system','1. Keep soil consistently moist (not soggy)\r\n2. Mist leaves 2-3 times weekly\r\n3. Fertilize monthly during growing season\r\n4. Wipe leaves with damp cloth to remove dust\r\n5. Remove spent flowers at base\r\n6. Keep away from direct sunlight',3),(3,' Tomato (Solanum lycopersicum)','Fruiting plant','Trowel: For digging and planting seeds\r\nWatering Can: For watering the plants\r\nPruners: For trimming and shaping the plants\r\nGarden Fork: For turning soil and breaking up clumps               Potting Soil: Provides nutrients and support for the plants\r\nFertilizer: Enhances growth and fruit production\r\nMulch: Helps retain moisture and suppress weeds','Seeds: The starting point for growth\r\nRoots: Anchor the plant and absorb water and nutrients\r\nStems: Support the plant and transport nutrients\r\nLeaves: Conduct photosynthesis and provide energy','Seed Preparation: Start by selecting high-quality seeds and soaking them in water for a few hours to enhance germination.\r\n\r\nSoil Preparation: Fill pots or garden beds with potting soil, ensuring it is well-aerated and free of debris.\r\n\r\nPlanting Seeds: Plant seeds about 1/4 inch deep in the soil, spacing them according to the seed packet instructions.\r\n\r\nWatering: Water the seeds gently using a watering can, ensuring the soil is moist but not waterlogged.\r\n\r\nSunlight: Place the pots in a sunny location or under grow lights, providing at least 6-8 hours of sunlight daily.\r\n\r\nThinning: Once seedlings emerge, thin them out to prevent overcrowding, leaving the strongest plants.\r\n\r\nFertilizing: Apply fertilizer every few weeks according to the product instructions to promote healthy growth.\r\n\r\nPruning: As the plants grow, prune excess leaves and suckers to encourage better air circulation and fruit production.\r\n\r\nHarvesting: Once the tomatoes are ripe, harvest them by cutting the stem with pruners, ensuring to handle them gently to avoid bruising.',3);
/*!40000 ALTER TABLE `plant` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-23  1:19:29
