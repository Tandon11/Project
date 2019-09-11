-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 11, 2019 at 08:14 AM
-- Server version: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `key_logger_beta`
--

-- --------------------------------------------------------

--
-- Table structure for table `active_window`
--

CREATE TABLE `active_window` (
  `sr` int(11) NOT NULL,
  `start` bigint(20) NOT NULL,
  `end` bigint(20) NOT NULL,
  `duration` bigint(20) NOT NULL,
  `title` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `active_window`
--

INSERT INTO `active_window` (`sr`, `start`, `end`, `duration`, `title`) VALUES
(142, 1532337454296, 1532337456318, 2, 'KeyLogger - NetBeans IDE 8.2'),
(143, 1532337456318, 1532337459478, 3, 'Cortana'),
(144, 1532337459478, 1532337463870, 4, 'Untitled - Notepad'),
(145, 1532337463870, 1532337465206, 1, 'Notepad');

-- --------------------------------------------------------

--
-- Table structure for table `insertion`
--

CREATE TABLE `insertion` (
  `sr` int(11) NOT NULL,
  `char1` varchar(20) NOT NULL,
  `time1` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `insertion`
--

INSERT INTO `insertion` (`sr`, `char1`, `time1`) VALUES
(618, 'N', 1531504130605),
(619, 'O', 1531504130829),
(620, 'T', 1531504131195),
(621, 'E', 1531504131564),
(622, 'P', 1531504131725),
(623, 'A', 1531504132045),
(624, 'D', 1531504132296),
(625, 'Z', 1531504136615),
(626, 'X', 1531504136796),
(627, 'C', 1531504137025),
(628, 'V', 1531504137256),
(629, 'B', 1531504137506),
(630, 'N', 1531504137746),
(631, 'N', 1532264175890),
(632, 'O', 1532264176084),
(633, 'T', 1532264176521),
(634, 'E', 1532264177035),
(635, 'P', 1532264177220),
(636, 'A', 1532264177420),
(637, 'D', 1532264177740),
(638, 'D', 1532264181916),
(639, 'D', 1532264181941),
(640, 'F', 1532264182031),
(641, 'B', 1532264182111),
(642, 'E', 1532264182151),
(643, 'V', 1532264182251),
(644, 'H', 1532264182275),
(645, 'V', 1532264182400),
(646, 'B', 1532264182411),
(647, 'D', 1532264182481),
(648, 'C', 1532264182551),
(649, 'B', 1532264182611),
(650, 'W', 1532264182641),
(651, 'D', 1532264182650),
(652, 'C', 1532264182701),
(653, 'J', 1532264182751),
(654, 'K', 1532264182762),
(655, 'D', 1532264182791),
(656, 'C', 1532264182870),
(657, 'Space', 1532264183270),
(658, 'Enter', 1532264183455),
(659, 'D', 1532264183621),
(660, 'V', 1532264183681),
(661, 'Enter', 1532264183791),
(662, 'D', 1532264183821),
(663, 'F', 1532264183839),
(664, 'V', 1532264183891),
(665, 'F', 1532264183981),
(666, 'V', 1532264184041),
(667, 'F', 1532264184133),
(668, 'D', 1532264184170),
(669, 'Enter', 1532264184180),
(670, 'V', 1532264184240),
(671, 'D', 1532264184333),
(672, 'F', 1532264184353),
(673, 'V', 1532264184430),
(674, 'D', 1532264184511),
(675, 'F', 1532264184551),
(676, 'V', 1532264184691),
(677, 'D', 1532264184695),
(678, 'F', 1532264184721),
(679, 'V', 1532264184770),
(680, 'R', 1532264184892);

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `knd` int(11) NOT NULL,
  `keytyped` text NOT NULL,
  `time` bigint(20) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`knd`, `keytyped`, `time`, `timestamp`) VALUES
(117, 'N', 1532337456805, '2018-07-23 09:17:36'),
(118, 'O', 1532337457064, '2018-07-23 09:17:37'),
(119, 'T', 1532337457333, '2018-07-23 09:17:37'),
(120, 'E', 1532337457507, '2018-07-23 09:17:37'),
(121, 'P', 1532337457653, '2018-07-23 09:17:37'),
(122, 'A', 1532337457823, '2018-07-23 09:17:37'),
(123, 'D', 1532337457993, '2018-07-23 09:17:38'),
(124, 'Enter', 1532337458647, '2018-07-23 09:17:38'),
(125, 'A', 1532337460083, '2018-07-23 09:17:40'),
(126, 'S', 1532337460219, '2018-07-23 09:17:40'),
(127, 'D', 1532337460416, '2018-07-23 09:17:40'),
(128, 'F', 1532337460560, '2018-07-23 09:17:40');

-- --------------------------------------------------------

--
-- Table structure for table `words`
--

CREATE TABLE `words` (
  `s.no.` int(11) NOT NULL,
  `title` text NOT NULL,
  `stime` time NOT NULL,
  `etime` time NOT NULL,
  `words` text NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `words`
--

INSERT INTO `words` (`s.no.`, `title`, `stime`, `etime`, `words`, `date`) VALUES
(266, 'title', '10:12:12', '12:12:12', 'gffdfgdf', '2012-12-12'),
(267, 'appscreen - NetBeans IDE 8.2', '23:18:48', '23:18:49', '', '2013-07-18'),
(268, 'Cortana', '23:18:49', '23:18:55', 'NOTEPAD', '2013-07-18'),
(269, 'Untitled - Notepad', '23:18:55', '23:19:00', 'ZXCVBN', '2013-07-18'),
(270, 'appscreen - NetBeans IDE 8.2', '23:18:48', '23:18:49', '', '2013-07-18'),
(271, 'Cortana', '23:18:49', '23:18:55', 'NOTEPAD', '2013-07-18'),
(272, 'Untitled - Notepad', '23:18:55', '23:19:00', 'ZXCVBN', '2013-07-18'),
(273, 'appscreen - NetBeans IDE 8.2', '18:26:12', '18:26:13', '', '2022-07-18'),
(274, 'Cortana', '18:26:13', '18:26:21', 'NOTEPAD', '2022-07-18'),
(275, 'Untitled - Notepad', '18:26:21', '18:26:26', 'DDFBEVHVBDCBWDCJKDC EnterDVEnterDFVFVFDEnterVDFVDFVDFVR', '2022-07-18'),
(276, 'Notepad', '18:26:26', '18:26:29', '', '2022-07-18');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `active_window`
--
ALTER TABLE `active_window`
  ADD PRIMARY KEY (`sr`);

--
-- Indexes for table `insertion`
--
ALTER TABLE `insertion`
  ADD PRIMARY KEY (`sr`);

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`knd`);

--
-- Indexes for table `words`
--
ALTER TABLE `words`
  ADD PRIMARY KEY (`s.no.`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `active_window`
--
ALTER TABLE `active_window`
  MODIFY `sr` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=146;
--
-- AUTO_INCREMENT for table `insertion`
--
ALTER TABLE `insertion`
  MODIFY `sr` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=681;
--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `knd` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=129;
--
-- AUTO_INCREMENT for table `words`
--
ALTER TABLE `words`
  MODIFY `s.no.` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=277;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
