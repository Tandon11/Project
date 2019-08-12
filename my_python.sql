-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 12, 2019 at 07:58 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `my_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `information`
--

CREATE TABLE `information` (
  `S.No` int(2) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Age` int(3) NOT NULL,
  `Gender` varchar(6) NOT NULL,
  `Hobbies` varchar(30) NOT NULL,
  `Qualification` varchar(20) NOT NULL,
  `Favfood` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `information`
--

INSERT INTO `information` (`S.No`, `Name`, `Age`, `Gender`, `Hobbies`, `Qualification`, `Favfood`) VALUES
(2, 'Abhishek', 21, 'male', 'cricket', 'engineering', 'pizza'),
(3, 'Rahul', 15, 'male', 'football', '10th', 'noodles'),
(4, 'Shikha', 30, 'female', 'singing', 'masters', 'indian'),
(5, 'Priya', 25, 'female', 'dancing', 'diploma', 'pasta'),
(6, 'Zaheer', 30, 'male', 'tennis', 'medical', 'italian'),
(7, 'Chandrakant', 19, 'male', 'squash', 'engineering', 'indian'),
(8, 'Anugrah', 22, 'male', 'photography', 'doctorate', 'chinese'),
(9, 'Vaibhav', 60, 'male', 'badminton', 'medical', 'continental'),
(10, 'Bhaskar', 23, 'male', 'squash', 'engineering', 'indian');

-- --------------------------------------------------------

--
-- Table structure for table `snake`
--

CREATE TABLE `snake` (
  `S.No` int(11) NOT NULL,
  `score` varchar(10) NOT NULL,
  `dt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `snake`
--

INSERT INTO `snake` (`S.No`, `score`, `dt`) VALUES
(1, '3', '2019-07-20 07:58:39'),
(2, '10', '2019-07-21 05:58:39'),
(3, '27', '2019-07-25 15:15:50'),
(4, '8', '2019-07-25 15:20:39'),
(5, '30', '2019-08-10 06:47:49'),
(6, '18', '2019-08-10 06:50:09'),
(7, '9', '2019-08-10 06:57:11'),
(8, '23', '2019-08-10 07:00:21');

-- --------------------------------------------------------

--
-- Table structure for table `weather`
--

CREATE TABLE `weather` (
  `S.No` int(11) NOT NULL,
  `conditions` varchar(50) NOT NULL,
  `temperature` varchar(50) NOT NULL,
  `pressure` varchar(50) NOT NULL,
  `humidity` varchar(50) NOT NULL,
  `speed` varchar(50) NOT NULL,
  `angle` varchar(50) NOT NULL,
  `datetime` varchar(50) NOT NULL,
  `place` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `weather`
--

INSERT INTO `weather` (`S.No`, `conditions`, `temperature`, `pressure`, `humidity`, `speed`, `angle`, `datetime`, `place`) VALUES
(1, 'moderate rain', '30degree celsius', '1000.84milli Bar', '70percent', '2.64meter per second', '14.478degree', '2019-07-19 23:52:39.704006', 'Raipur'),
(2, 'clear sky', '34degree celsius', '1002.34milli Bar', '47percent', '4.34meter per second', '82.656degree', '2019-07-20 10:41:33.925272', 'Delhi'),
(3, 'scattered clouds', '30degree celsius', '1004milli Bar', '79percent', '2.6meter per second', '90degree', '2019-07-20 13:08:55.113581', 'Patna'),
(4, 'scattered clouds', '30degree celsius', '1004milli Bar', '79percent', '2.6meter per second', '90degree', '2019-07-20 13:09:28.507893', 'Patna'),
(5, 'scattered clouds', '30degree celsius', '1004milli Bar', '79percent', '2.6meter per second', '90degree', '2019-07-20 13:10:08.400610', 'Patna'),
(6, 'overcast clouds', '35degree celsius', '999.85milli Bar', '40percent', '2.6meter per second', '79.421degree', '2019-07-20 13:13:55.956877', 'Mumbai'),
(7, 'few clouds', '26degree celsius', '1001.61milli Bar', '84percent', '3.25meter per second', '218.971degree', '2019-08-09 21:27:59.500520', 'Raipur');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `information`
--
ALTER TABLE `information`
  ADD PRIMARY KEY (`S.No`);

--
-- Indexes for table `snake`
--
ALTER TABLE `snake`
  ADD PRIMARY KEY (`S.No`);

--
-- Indexes for table `weather`
--
ALTER TABLE `weather`
  ADD PRIMARY KEY (`S.No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `information`
--
ALTER TABLE `information`
  MODIFY `S.No` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `snake`
--
ALTER TABLE `snake`
  MODIFY `S.No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `weather`
--
ALTER TABLE `weather`
  MODIFY `S.No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
