-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-09-2020 a las 03:13:23
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.1.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `idoctorv2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignacioninternados`
--

CREATE TABLE `asignacioninternados` (
  `idAsignInternado` int(10) NOT NULL,
  `idInternado` int(10) NOT NULL,
  `idUsuario` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `asignacioninternados`
--

INSERT INTO `asignacioninternados` (`idAsignInternado`, `idInternado`, `idUsuario`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultas`
--

CREATE TABLE `consultas` (
  `idConsulta` int(10) NOT NULL,
  `idConsultorio` int(10) NOT NULL,
  `idPaciente` int(10) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `diagnostico` varchar(110) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `consultas`
--

INSERT INTO `consultas` (`idConsulta`, `idConsultorio`, `idPaciente`, `fecha`, `hora`, `diagnostico`) VALUES
(1, 1, 2, '2020-09-30', '20:19:00', NULL),
(2, 1, 4, '2020-08-04', '32:23:00', 'diagnostico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultorios`
--

CREATE TABLE `consultorios` (
  `idConsultorio` int(10) NOT NULL,
  `idUsuario` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `consultorios`
--

INSERT INTO `consultorios` (`idConsultorio`, `idUsuario`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `examenes`
--

CREATE TABLE `examenes` (
  `idExamen` int(10) NOT NULL,
  `Nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `examenes`
--

INSERT INTO `examenes` (`idExamen`, `Nombre`) VALUES
(1, 'Resonancia Magnetica'),
(2, 'Prueba Embarazo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habitaciones`
--

CREATE TABLE `habitaciones` (
  `idHabitacion` int(10) NOT NULL,
  `disponibilidad` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `habitaciones`
--

INSERT INTO `habitaciones` (`idHabitacion`, `disponibilidad`) VALUES
(1, 1),
(2, 0),
(3, 1),
(4, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historialexamenes`
--

CREATE TABLE `historialexamenes` (
  `idHistorialExamen` int(10) NOT NULL,
  `fechaSolicitud` date NOT NULL,
  `comentario` varchar(50) NOT NULL,
  `idUsuario` int(10) NOT NULL,
  `idPaciente` int(10) NOT NULL,
  `idExamen` int(10) NOT NULL,
  `resultados` varchar(100) NOT NULL,
  `status` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `historialexamenes`
--

INSERT INTO `historialexamenes` (`idHistorialExamen`, `fechaSolicitud`, `comentario`, `idUsuario`, `idPaciente`, `idExamen`, `resultados`, `status`) VALUES
(1, '2020-09-22', 'asdfasdf', 2, 3, 1, '', 0),
(2, '2020-07-01', 'comentario exmane', 2, 4, 1, 'resultados examen ', 2),
(3, '2020-09-01', 'comentario exmane', 1, 4, 1, 'res', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `internados`
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
-- Volcado de datos para la tabla `internados`
--

INSERT INTO `internados` (`idInternado`, `idPaciente`, `idHabitacion`, `fechaIngreso`, `fechaAlta`, `idTipoInternado`) VALUES
(1, 2, 2, '2020-09-02', NULL, 1),
(2, 4, 1, '2020-09-01', '2020-09-12', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
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
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`idPaciente`, `nombreCompleto`, `fechaNacimiento`, `Sexo`, `lugarNacimiento`, `CURP`, `grupoSanguineo`, `enfermedadesPree`, `alergias`, `direccionPaciente`, `contactoPaciente`, `contactoReferencias`, `idTipoPaciente`) VALUES
(1, 'David Zumano', '2020-09-01', 'F', 'Obrera', 't34f34f34fd34f34', 'AB-', '-', '-', '-', '-', '44512223', 1),
(2, 'Poncho Rivera', '1990-10-03', 'M', 'Hidalgo', 'curpgenerica', 'O+', '-', '-', '-', '-', '-', 2),
(3, 'jose david', '2004-06-22', 'H', 'CDMX', 'curpaadsfasdf', 'A+', 'preexis', 'alergias', 'direccion', '444422', '4442545R', 1),
(4, 'david david', '2000-06-09', 'n', 'qro', 'curpasdf', 'A+', 'mimguna', 'no alergias', 'luis quintero', '4427444', '42274RR', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipointernados`
--

CREATE TABLE `tipointernados` (
  `idTipoInternado` int(10) NOT NULL,
  `tipoInternado` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipointernados`
--

INSERT INTO `tipointernados` (`idTipoInternado`, `tipoInternado`) VALUES
(1, 'Cuidados Intensivo'),
(2, 'Quirofano'),
(3, 'Piso');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipopacientes`
--

CREATE TABLE `tipopacientes` (
  `idTipoPaciente` int(10) NOT NULL,
  `nombre` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipopacientes`
--

INSERT INTO `tipopacientes` (`idTipoPaciente`, `nombre`) VALUES
(1, 'Transitorio'),
(2, 'Internado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiposusuario`
--

CREATE TABLE `tiposusuario` (
  `idTipo` int(10) NOT NULL,
  `tipoUsuario` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tiposusuario`
--

INSERT INTO `tiposusuario` (`idTipo`, `tipoUsuario`) VALUES
(1, 'Doctor'),
(2, 'Enfermero'),
(3, 'Laborista'),
(4, 'Administrador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
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
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `nombreUsuario`, `apellidoUsuario`, `emailUsuario`, `password`, `idTipo`) VALUES
(1, 'Hugo', 'Gonzalez', 'hhav21@outlook.com', '$2b$12$EjdR07sarlMmOLCA3e7HX.CahxU3PU6.JgXm.YI/E0TyidG44pZBe', 1),
(2, 'david', 'lozano', 'david_7nike@hotmail.com', '$2b$12$KMlP22LzeT89YhoxOFxX4.HXEsLD/ma.lHl9l9iTN4IpCKdhes9dS', 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asignacioninternados`
--
ALTER TABLE `asignacioninternados`
  ADD PRIMARY KEY (`idAsignInternado`),
  ADD KEY `idUsuario` (`idUsuario`),
  ADD KEY `idInternado` (`idInternado`);

--
-- Indices de la tabla `consultas`
--
ALTER TABLE `consultas`
  ADD PRIMARY KEY (`idConsulta`),
  ADD KEY `idConsultorio` (`idConsultorio`),
  ADD KEY `idPaciente` (`idPaciente`);

--
-- Indices de la tabla `consultorios`
--
ALTER TABLE `consultorios`
  ADD PRIMARY KEY (`idConsultorio`),
  ADD KEY `idUsuario` (`idUsuario`);

--
-- Indices de la tabla `examenes`
--
ALTER TABLE `examenes`
  ADD PRIMARY KEY (`idExamen`);

--
-- Indices de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD PRIMARY KEY (`idHabitacion`);

--
-- Indices de la tabla `historialexamenes`
--
ALTER TABLE `historialexamenes`
  ADD PRIMARY KEY (`idHistorialExamen`),
  ADD KEY `idUsuario` (`idUsuario`),
  ADD KEY `idPaciente` (`idPaciente`),
  ADD KEY `idExamen` (`idExamen`);

--
-- Indices de la tabla `internados`
--
ALTER TABLE `internados`
  ADD PRIMARY KEY (`idInternado`),
  ADD KEY `idPaciente` (`idPaciente`),
  ADD KEY `idHabitacion` (`idHabitacion`),
  ADD KEY `idTipoInternado` (`idTipoInternado`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`idPaciente`),
  ADD KEY `idTipoPaciente` (`idTipoPaciente`);

--
-- Indices de la tabla `tipointernados`
--
ALTER TABLE `tipointernados`
  ADD PRIMARY KEY (`idTipoInternado`);

--
-- Indices de la tabla `tipopacientes`
--
ALTER TABLE `tipopacientes`
  ADD PRIMARY KEY (`idTipoPaciente`);

--
-- Indices de la tabla `tiposusuario`
--
ALTER TABLE `tiposusuario`
  ADD PRIMARY KEY (`idTipo`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`),
  ADD KEY `idTipo` (`idTipo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asignacioninternados`
--
ALTER TABLE `asignacioninternados`
  MODIFY `idAsignInternado` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `consultas`
--
ALTER TABLE `consultas`
  MODIFY `idConsulta` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `consultorios`
--
ALTER TABLE `consultorios`
  MODIFY `idConsultorio` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `examenes`
--
ALTER TABLE `examenes`
  MODIFY `idExamen` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  MODIFY `idHabitacion` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `historialexamenes`
--
ALTER TABLE `historialexamenes`
  MODIFY `idHistorialExamen` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `internados`
--
ALTER TABLE `internados`
  MODIFY `idInternado` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `idPaciente` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tipointernados`
--
ALTER TABLE `tipointernados`
  MODIFY `idTipoInternado` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tipopacientes`
--
ALTER TABLE `tipopacientes`
  MODIFY `idTipoPaciente` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tiposusuario`
--
ALTER TABLE `tiposusuario`
  MODIFY `idTipo` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignacioninternados`
--
ALTER TABLE `asignacioninternados`
  ADD CONSTRAINT `asignacioninternados_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`),
  ADD CONSTRAINT `asignacioninternados_ibfk_2` FOREIGN KEY (`idInternado`) REFERENCES `internados` (`idInternado`);

--
-- Filtros para la tabla `consultas`
--
ALTER TABLE `consultas`
  ADD CONSTRAINT `consultas_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `pacientes` (`idPaciente`),
  ADD CONSTRAINT `consultas_ibfk_2` FOREIGN KEY (`idConsultorio`) REFERENCES `consultorios` (`idConsultorio`);

--
-- Filtros para la tabla `consultorios`
--
ALTER TABLE `consultorios`
  ADD CONSTRAINT `consultorios_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`);

--
-- Filtros para la tabla `historialexamenes`
--
ALTER TABLE `historialexamenes`
  ADD CONSTRAINT `historialexamenes_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `pacientes` (`idPaciente`),
  ADD CONSTRAINT `historialexamenes_ibfk_2` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`),
  ADD CONSTRAINT `historialexamenes_ibfk_3` FOREIGN KEY (`idExamen`) REFERENCES `examenes` (`idExamen`);

--
-- Filtros para la tabla `internados`
--
ALTER TABLE `internados`
  ADD CONSTRAINT `internados_ibfk_1` FOREIGN KEY (`idTipoInternado`) REFERENCES `tipointernados` (`idTipoInternado`),
  ADD CONSTRAINT `internados_ibfk_2` FOREIGN KEY (`idPaciente`) REFERENCES `pacientes` (`idPaciente`),
  ADD CONSTRAINT `internados_ibfk_3` FOREIGN KEY (`idHabitacion`) REFERENCES `habitaciones` (`idHabitacion`);

--
-- Filtros para la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD CONSTRAINT `pacientes_ibfk_1` FOREIGN KEY (`idTipoPaciente`) REFERENCES `tipopacientes` (`idTipoPaciente`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`idTipo`) REFERENCES `tiposusuario` (`idTipo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
