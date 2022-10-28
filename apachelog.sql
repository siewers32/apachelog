-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 28 okt 2022 om 11:22
-- Serverversie: 10.4.21-MariaDB-log
-- PHP-versie: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `apachelog`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `apache_log`
--

CREATE TABLE `apache_log` (
  `log_id` int(11) NOT NULL,
  `time` datetime DEFAULT NULL,
  `len` int(11) DEFAULT NULL,
  `useragent` varchar(255) DEFAULT NULL,
  `page` varchar(255) DEFAULT NULL,
  `method` varchar(45) DEFAULT NULL,
  `protocol` varchar(45) DEFAULT NULL,
  `log` varchar(255) DEFAULT NULL,
  `ip` varchar(24) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `apache_log`
--
ALTER TABLE `apache_log`
  ADD PRIMARY KEY (`log_id`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `apache_log`
--
ALTER TABLE `apache_log`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
