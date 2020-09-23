-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 23, 2020 at 04:39 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `iDoctorv2`
--

-- --------------------------------------------------------

--
-- Table structure for table `asignacionInternados`
--

CREATE TABLE `asignacionInternados` (
  `idAsignInternado` int(10) NOT NULL,
  `idInternado` int(10) NOT NULL,
  `idUsuario` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `asignacionInternados`
--

INSERT INTO `asignacionInternados` (`idAsignInternado`, `idInternado`, `idUsuario`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `consultas`
--

CREATE TABLE `consultas` (
  `idConsulta` int(10) NOT NULL,
  `idConsultorio` int(10) NOT NULL,
  `idPaciente` int(10) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `diagnostico` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `consultas`
--

INSERT INTO `consultas` (`idConsulta`, `idConsultorio`, `idPaciente`, `fecha`, `hora`, `diagnostico`) VALUES
(1, 1, 1, '2020-09-30', '20:19:00', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `consultorios`
--

CREATE TABLE `consultorios` (
  `idConsultorio` int(10) NOT NULL,
  `idUsuario` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `consultorios`
--

INSERT INTO `consultorios` (`idConsultorio`, `idUsuario`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `examenes`
--

CREATE TABLE `examenes` (
  `idExamen` int(10) NOT NULL,
  `Nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `examenes`
--

INSERT INTO `examenes` (`idExamen`, `Nombre`) VALUES
(1, 'Resonancia Magnetica'),
(2, 'Prueba Embarazo'),
(3, 'Radiografia'),
(4, 'Electrocardiograma');

-- --------------------------------------------------------

--
-- Table structure for table `habitaciones`
--

CREATE TABLE `habitaciones` (
  `idHabitacion` int(10) NOT NULL,
  `disponibilidad` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `habitaciones`
--

INSERT INTO `habitaciones` (`idHabitacion`, `disponibilidad`) VALUES
(1, 1),
(2, 0),
(3, 1),
(4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `historialExamenes`
--

CREATE TABLE `historialExamenes` (
  `idHistorialExamen` int(10) NOT NULL,
  `fechaSolicitud` date NOT NULL,
  `comentario` varchar(50) NOT NULL,
  `idUsuario` int(10) NOT NULL,
  `idPaciente` int(10) NOT NULL,
  `idExamen` int(10) NOT NULL,
  `resultados` varchar(100) DEFAULT NULL,
  `status` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `historialExamenes`
--

INSERT INTO `historialExamenes` (`idHistorialExamen`, `fechaSolicitud`, `comentario`, `idUsuario`, `idPaciente`, `idExamen`, `resultados`, `status`) VALUES
(1, '2020-09-22', '-', 1, 1, 4, NULL, 0),
(2, '2020-09-22', 'Urgente', 1, 2, 2, 'Positivo a embarazo', 1),
(3, '2020-09-22', 'Urgente', 1, 1, 3, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `internados`
--

CREATE TABLE `internados` (
  `idInternado` int(10) NOT NULL,
  `idPaciente` int(10) DEFAULT NULL,
  `idHabitacion` int(10) DEFAULT NULL,
  `fechaIngreso` date DEFAULT NULL,
  `fechaAlta` date DEFAULT NULL,
  `idTipoInternado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `internados`
--

INSERT INTO `internados` (`idInternado`, `idPaciente`, `idHabitacion`, `fechaIngreso`, `fechaAlta`, `idTipoInternado`) VALUES
(1, 2, 2, '2020-09-02', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `pacientes`
--

CREATE TABLE `pacientes` (
  `idPaciente` int(10) NOT NULL,
  `nombreCompleto` varchar(100) DEFAULT NULL,
  `fechaNacimiento` date NOT NULL,
  `Sexo` varchar(1) DEFAULT NULL,
  `lugarNacimiento` varchar(100) DEFAULT NULL,
  `CURP` varchar(30) DEFAULT NULL,
  `grupoSanguineo` varchar(10) DEFAULT NULL,
  `enfermedadesPree` varchar(200) DEFAULT NULL,
  `alergias` varchar(200) DEFAULT NULL,
  `direccionPaciente` varchar(100) DEFAULT NULL,
  `contactoPaciente` varchar(30) DEFAULT NULL,
  `contactoReferencias` varchar(11) DEFAULT NULL,
  `idTipoPaciente` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pacientes`
--

INSERT INTO `pacientes` (`idPaciente`, `nombreCompleto`, `fechaNacimiento`, `Sexo`, `lugarNacimiento`, `CURP`, `grupoSanguineo`, `enfermedadesPree`, `alergias`, `direccionPaciente`, `contactoPaciente`, `contactoReferencias`, `idTipoPaciente`) VALUES
(1, 'David Zumano', '2020-09-01', 'F', 'Obrera', 't34f34f34fd34f34', 'AB-', '-', '-', '-', '-', '44512223', 1),
(2, 'Poncho Rivera', '1990-10-03', 'M', 'Hidalgo', 'curpgenerica', 'O+', '-', '-', '-', '-', '-', 2);

-- --------------------------------------------------------

--
-- Table structure for table `tipoInternados`
--

CREATE TABLE `tipoInternados` (
  `idTipoInternado` int(10) NOT NULL,
  `tipoInternado` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tipoInternados`
--

INSERT INTO `tipoInternados` (`idTipoInternado`, `tipoInternado`) VALUES
(1, 'Cuidados Intensivo'),
(2, 'Quirofano'),
(3, 'Piso');

-- --------------------------------------------------------

--
-- Table structure for table `tipoPacientes`
--

CREATE TABLE `tipoPacientes` (
  `idTipoPaciente` int(10) NOT NULL,
  `nombre` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tipoPacientes`
--

INSERT INTO `tipoPacientes` (`idTipoPaciente`, `nombre`) VALUES
(1, 'Transitorio'),
(2, 'Internado');

-- --------------------------------------------------------

--
-- Table structure for table `tiposUsuario`
--

CREATE TABLE `tiposUsuario` (
  `idTipo` int(10) NOT NULL,
  `tipoUsuario` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tiposUsuario`
--

INSERT INTO `tiposUsuario` (`idTipo`, `tipoUsuario`) VALUES
(1, 'Doctor'),
(2, 'Enfermero'),
(3, 'Laborista'),
(4, 'Administrador');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(10) NOT NULL,
  `nombreUsuario` varchar(50) DEFAULT NULL,
  `apellidoUsuario` varchar(50) DEFAULT NULL,
  `emailUsuario` varchar(50) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `idTipo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `nombreUsuario`, `apellidoUsuario`, `emailUsuario`, `password`, `idTipo`) VALUES
(1, 'Hugo', 'Gonzalez', 'hhav21@outlook.com', '$2b$12$EjdR07sarlMmOLCA3e7HX.CahxU3PU6.JgXm.YI/E0TyidG44pZBe', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `asignacionInternados`
--
ALTER TABLE `asignacionInternados`
  ADD PRIMARY KEY (`idAsignInternado`);

--
-- Indexes for table `consultas`
--
ALTER TABLE `consultas`
  ADD PRIMARY KEY (`idConsulta`);

--
-- Indexes for table `consultorios`
--
ALTER TABLE `consultorios`
  ADD PRIMARY KEY (`idConsultorio`);

--
-- Indexes for table `examenes`
--
ALTER TABLE `examenes`
  ADD PRIMARY KEY (`idExamen`);

--
-- Indexes for table `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD PRIMARY KEY (`idHabitacion`);

--
-- Indexes for table `historialExamenes`
--
ALTER TABLE `historialExamenes`
  ADD PRIMARY KEY (`idHistorialExamen`);

--
-- Indexes for table `internados`
--
ALTER TABLE `internados`
  ADD PRIMARY KEY (`idInternado`);

--
-- Indexes for table `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`idPaciente`);

--
-- Indexes for table `tipoInternados`
--
ALTER TABLE `tipoInternados`
  ADD PRIMARY KEY (`idTipoInternado`);

--
-- Indexes for table `tipoPacientes`
--
ALTER TABLE `tipoPacientes`
  ADD PRIMARY KEY (`idTipoPaciente`);

--
-- Indexes for table `tiposUsuario`
--
ALTER TABLE `tiposUsuario`
  ADD PRIMARY KEY (`idTipo`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `asignacionInternados`
--
ALTER TABLE `asignacionInternados`
  MODIFY `idAsignInternado` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `consultas`
--
ALTER TABLE `consultas`
  MODIFY `idConsulta` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `consultorios`
--
ALTER TABLE `consultorios`
  MODIFY `idConsultorio` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `examenes`
--
ALTER TABLE `examenes`
  MODIFY `idExamen` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `habitaciones`
--
ALTER TABLE `habitaciones`
  MODIFY `idHabitacion` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `historialExamenes`
--
ALTER TABLE `historialExamenes`
  MODIFY `idHistorialExamen` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `internados`
--
ALTER TABLE `internados`
  MODIFY `idInternado` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `idPaciente` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tipoInternados`
--
ALTER TABLE `tipoInternados`
  MODIFY `idTipoInternado` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tipoPacientes`
--
ALTER TABLE `tipoPacientes`
  MODIFY `idTipoPaciente` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tiposUsuario`
--
ALTER TABLE `tiposUsuario`
  MODIFY `idTipo` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
