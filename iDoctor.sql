-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 21, 2020 at 12:34 AM
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
-- Database: `iDoctor`
--

-- --------------------------------------------------------

--
-- Table structure for table `consulta`
--

CREATE TABLE `consulta` (
  `idConsulta` int(11) NOT NULL,
  `hora` time NOT NULL,
  `fecha` date NOT NULL,
  `idDoctor` int(11) NOT NULL,
  `idPaciente` int(11) NOT NULL,
  `idExamen` int(11) NOT NULL,
  `idConsultorio` int(11) NOT NULL,
  `idEnfermero` int(11) NOT NULL,
  `idHabitacion` int(11) NOT NULL,
  `status` varchar(100) NOT NULL,
  `comentario` varchar(500) NOT NULL,
  `folioExamen` int(11) NOT NULL,
  `resultadoExamen` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `consulta`
--

INSERT INTO `consulta` (`idConsulta`, `hora`, `fecha`, `idDoctor`, `idPaciente`, `idExamen`, `idConsultorio`, `idEnfermero`, `idHabitacion`, `status`, `comentario`, `folioExamen`, `resultadoExamen`) VALUES
(1, '20:16:06', '2020-09-09', 1, 1, 1, 1, 1, 1, '0', 'comentario onsulta', 12548, 'resultado examen');

-- --------------------------------------------------------

--
-- Table structure for table `consultorio`
--

CREATE TABLE `consultorio` (
  `idConsultorio` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `consultorio`
--

INSERT INTO `consultorio` (`idConsultorio`) VALUES
(1),
(2),
(3);

-- --------------------------------------------------------

--
-- Table structure for table `doctores`
--

CREATE TABLE `doctores` (
  `idDoctor` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `contadorPaciente` int(50) NOT NULL,
  `especialidad` varchar(100) NOT NULL,
  `contacto` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `doctores`
--

INSERT INTO `doctores` (`idDoctor`, `nombre`, `contadorPaciente`, `especialidad`, `contacto`) VALUES
(1, 'dr mario', 0, 'en las chivas', '4424545445');

-- --------------------------------------------------------

--
-- Table structure for table `enfermeros`
--

CREATE TABLE `enfermeros` (
  `idenfermero` int(11) NOT NULL,
  `nombre` varchar(110) NOT NULL,
  `contadorPaciente` int(11) NOT NULL,
  `contacto` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `enfermeros`
--

INSERT INTO `enfermeros` (`idenfermero`, `nombre`, `contadorPaciente`, `contacto`) VALUES
(1, 'enfermero ivan', 0, '4425454');

-- --------------------------------------------------------

--
-- Table structure for table `examen`
--

CREATE TABLE `examen` (
  `idExamen` int(11) NOT NULL,
  `tipo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `examen`
--

INSERT INTO `examen` (`idExamen`, `tipo`) VALUES
(1, 'Examen de sangre'),
(2, 'Prueba de embarazo'),
(3, 'eletrocardiograma');

-- --------------------------------------------------------

--
-- Table structure for table `habitacion`
--

CREATE TABLE `habitacion` (
  `idHabitacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `habitacion`
--

INSERT INTO `habitacion` (`idHabitacion`) VALUES
(1);

-- --------------------------------------------------------

--
-- Table structure for table `historial`
--

CREATE TABLE `historial` (
  `idHistorial` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `comentario` varchar(200) NOT NULL,
  `idDoctor` int(11) NOT NULL,
  `idPaciente` int(11) NOT NULL,
  `idExamen` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `historial`
--

INSERT INTO `historial` (`idHistorial`, `fecha`, `comentario`, `idDoctor`, `idPaciente`, `idExamen`) VALUES
(5, '2020-09-20', 'Prueba', 8, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `paciente`
--

CREATE TABLE `paciente` (
  `idPaciente` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `fechaNacimiento` date NOT NULL,
  `sexo` varchar(100) NOT NULL,
  `lugarNaimiento` varchar(100) NOT NULL,
  `curp` varchar(100) NOT NULL,
  `grupoSanguineo` varchar(100) NOT NULL,
  `enfermedadesPre` varchar(100) NOT NULL,
  `alergias` varchar(100) NOT NULL,
  `contacto` varchar(100) NOT NULL,
  `contactoReferencia` varchar(100) NOT NULL,
  `transitorio` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `paciente`
--

INSERT INTO `paciente` (`idPaciente`, `nombre`, `fechaNacimiento`, `sexo`, `lugarNaimiento`, `curp`, `grupoSanguineo`, `enfermedadesPre`, `alergias`, `contacto`, `contactoReferencia`, `transitorio`) VALUES
(1, 'hugo', '2020-09-05', 'm', 'qro', 'asdfghj', 'a', '-', '-', '425156', '4444', 0),
(2, 'BIcho', '2020-09-08', 'm', 'obrera', '-', '-', '-', '-', '-', '-', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tipo_usuario`
--

CREATE TABLE `tipo_usuario` (
  `id_tipo` int(11) NOT NULL,
  `tipoUsuario` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tipo_usuario`
--

INSERT INTO `tipo_usuario` (`id_tipo`, `tipoUsuario`) VALUES
(1, 'Doctor'),
(2, 'Enfermero'),
(3, 'Laborista'),
(4, 'Administrador');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `nombreUsuario` varchar(100) NOT NULL,
  `apellidoUsuario` varchar(30) NOT NULL,
  `emailUsuario` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id_tipo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `nombreUsuario`, `apellidoUsuario`, `emailUsuario`, `password`, `id_tipo`) VALUES
(1, 'david', 'chavez', 'bicho@uaq.mx', '123', 1),
(8, 'Hugo', 'Villafuerte', 'hhav21@outlook.com', '$2b$12$EjdR07sarlMmOLCA3e7HX.CahxU3PU6.JgXm.YI/E0TyidG44pZBe', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `consulta`
--
ALTER TABLE `consulta`
  ADD PRIMARY KEY (`idConsulta`),
  ADD KEY `idDoctor` (`idDoctor`),
  ADD KEY `idPaciente` (`idPaciente`),
  ADD KEY `idExamen` (`idExamen`),
  ADD KEY `idConsultorio` (`idConsultorio`),
  ADD KEY `idEnfermero` (`idEnfermero`),
  ADD KEY `idHabitacion` (`idHabitacion`);

--
-- Indexes for table `consultorio`
--
ALTER TABLE `consultorio`
  ADD PRIMARY KEY (`idConsultorio`);

--
-- Indexes for table `doctores`
--
ALTER TABLE `doctores`
  ADD PRIMARY KEY (`idDoctor`);

--
-- Indexes for table `enfermeros`
--
ALTER TABLE `enfermeros`
  ADD PRIMARY KEY (`idenfermero`);

--
-- Indexes for table `examen`
--
ALTER TABLE `examen`
  ADD PRIMARY KEY (`idExamen`);

--
-- Indexes for table `habitacion`
--
ALTER TABLE `habitacion`
  ADD PRIMARY KEY (`idHabitacion`);

--
-- Indexes for table `historial`
--
ALTER TABLE `historial`
  ADD PRIMARY KEY (`idHistorial`);

--
-- Indexes for table `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`idPaciente`);

--
-- Indexes for table `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  ADD PRIMARY KEY (`id_tipo`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`),
  ADD KEY `id_tipo` (`id_tipo`) USING BTREE;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `consulta`
--
ALTER TABLE `consulta`
  MODIFY `idConsulta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `consultorio`
--
ALTER TABLE `consultorio`
  MODIFY `idConsultorio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `doctores`
--
ALTER TABLE `doctores`
  MODIFY `idDoctor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `enfermeros`
--
ALTER TABLE `enfermeros`
  MODIFY `idenfermero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `examen`
--
ALTER TABLE `examen`
  MODIFY `idExamen` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `habitacion`
--
ALTER TABLE `habitacion`
  MODIFY `idHabitacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `historial`
--
ALTER TABLE `historial`
  MODIFY `idHistorial` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `paciente`
--
ALTER TABLE `paciente`
  MODIFY `idPaciente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  MODIFY `id_tipo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `consulta`
--
ALTER TABLE `consulta`
  ADD CONSTRAINT `consulta_ibfk_1` FOREIGN KEY (`idDoctor`) REFERENCES `doctores` (`idDoctor`),
  ADD CONSTRAINT `consulta_ibfk_2` FOREIGN KEY (`idEnfermero`) REFERENCES `enfermeros` (`idenfermero`),
  ADD CONSTRAINT `consulta_ibfk_3` FOREIGN KEY (`idPaciente`) REFERENCES `paciente` (`idPaciente`),
  ADD CONSTRAINT `consulta_ibfk_4` FOREIGN KEY (`idHabitacion`) REFERENCES `habitacion` (`idHabitacion`),
  ADD CONSTRAINT `consulta_ibfk_5` FOREIGN KEY (`idConsultorio`) REFERENCES `consultorio` (`idConsultorio`),
  ADD CONSTRAINT `consulta_ibfk_6` FOREIGN KEY (`idExamen`) REFERENCES `examen` (`idExamen`);

--
-- Constraints for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_tipo`) REFERENCES `tipo_usuario` (`id_tipo`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
