-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 19, 2020 at 10:07 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 5.6.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `phone_num` varchar(20) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'Balaji Betadur', '08892011406', 'wer', '2020-01-15 23:41:24', 'balajibetadur@gmail.'),
(2, 'BALAJI YELLAPPA BETA', '08892011406', 'hry\r\n', '2020-01-16 00:03:42', 'balajibetadur@gmail.'),
(3, 'BALAJI YELLAPPA BETA', '08892011406', 'hry\r\n', '2020-01-16 00:04:10', 'balajibetadur@gmail.'),
(4, 'BALAJI YELLAPPA BETA', '08892011406', 'hry\r\n', '2020-01-16 00:05:17', 'balajibetadur@gmail.'),
(5, 'Balaji Betadur', '08892011406', 'bro', '2020-01-16 00:11:18', 'balajibetadur@gmail.'),
(6, 'Balaji Betadur', '08892011406', 'erereeeeeeeeeee', '2020-01-16 00:11:59', 'balajibetadur@gmail.'),
(7, 'Balaji Betadur', '08892011406', 'wq34', '2020-01-16 00:12:34', 'balajibetadur@gmail.'),
(8, 'qwr', 'wer', 'werwerwer', '2020-01-16 18:40:58', 'wr'),
(9, 'rtretretert', 'etert', 'e', '2020-01-16 18:41:32', 'ertertert');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(30) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(30) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(4, 'er', 'estr', 'st', 'sdt', 'sdrfer', '2020-01-16 19:08:15'),
(5, 'df', 'sf', 'sfsf', 'sdfsdfsdff', 'sdfsdfsdfsdfsdfsdfsdfsdfdsffff', '2020-01-16 19:10:19'),
(6, 'ewrewr', 'ewrwer', 'werwer', 'werwer', 'werwerwer', '2020-01-16 19:28:55'),
(7, 'kj', 'jk', 'yyy', 'cgf', 'tytty', '2020-01-19 11:56:10'),
(8, 'kj', 'jk', 'yyy', 'cgf', 'tytty', '2020-01-19 11:56:10'),
(9, 'test1', 'w', 'w', 'w', 'w', '2020-01-19 11:57:13'),
(10, 'test1', 'w', 'w', 'w', 'w', '2020-01-19 11:58:54'),
(11, 'ty', 'ty', 'ty', 'yu', 'ty', '2020-01-19 11:59:56'),
(12, 'iii', '', '', '', '', '2020-01-19 12:01:49');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
