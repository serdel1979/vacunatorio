-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 03-04-2022 a las 04:20:44
-- Versión del servidor: 10.3.31-MariaDB
-- Versión de PHP: 7.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdvacunatorio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos`
--

CREATE TABLE `turnos` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `fecha_solicitud` date NOT NULL,
  `fecha_turno` date NOT NULL,
  `sede` varchar(50) NOT NULL,
  `vacuna` varchar(50) NOT NULL,
  `estado` int(4) NOT NULL,
  `asistio` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `turnos`
--

INSERT INTO `turnos` (`id`, `id_usuario`, `fecha_solicitud`, `fecha_turno`, `sede`, `vacuna`, `estado`, `asistio`) VALUES
(1, 1, '2022-03-27', '2022-04-06', 'Cementerio', 'Fiebre amarilla', 0, 0),
(2, 1, '2022-03-27', '2022-04-13', 'Terminal', 'Gripe', 1, 0),
(3, 1, '2022-03-27', '2022-04-13', 'Cementerio', 'Gripe', 1, 0),
(4, 1, '2022-03-27', '2022-04-04', 'Municipal', 'Fiebre amarilla', 0, 0),
(5, 14, '2022-03-28', '2022-04-04', 'Cementerio', 'Gripe', 1, 0),
(6, 4, '2022-03-28', '2022-04-06', 'Terminal', 'Fiebre amarilla', 0, 0),
(7, 28, '2022-04-02', '2022-04-09', 'Terminal', 'Covid', 1, 0),
(8, 28, '2022-04-02', '2022-04-09', 'Terminal', 'Gripe', 1, 0),
(9, 28, '2022-04-03', '2022-04-13', 'Terminal', 'Fiebre amarilla', 1, 0),
(10, 26, '2022-04-03', '2022-04-11', 'Municipal', 'Gripe', 1, 0),
(11, 27, '2022-04-03', '2022-04-19', 'Terminal', 'Covid', 1, 0),
(12, 27, '2022-04-03', '2022-04-10', 'Cementerio', 'Gripe', 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `usuario` varchar(100) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `telefono` varchar(100) DEFAULT NULL,
  `nacimiento` date DEFAULT NULL,
  `primera_dosis` tinyint(1) DEFAULT NULL,
  `paciente_riesgo` tinyint(1) DEFAULT NULL,
  `fiebre_amarilla` tinyint(1) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `dni` varchar(100) DEFAULT NULL,
  `sede_preferida` varchar(100) DEFAULT NULL,
  `sede` varchar(100) DEFAULT NULL,
  `tipo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `usuario`, `nombre`, `apellido`, `telefono`, `nacimiento`, `primera_dosis`, `paciente_riesgo`, `fiebre_amarilla`, `password`, `email`, `dni`, `sede_preferida`, `sede`, `tipo`) VALUES
(1, 'kiko', 'federico', 'cuello', '221321321', '2010-05-11', 1, 1, 1, 'kiko', 'f@mail.com', '221321321', '', '0', 3),
(6, 'admin', 'administrador', 'administrador', NULL, NULL, NULL, NULL, NULL, 'admin', NULL, NULL, '', NULL, 1),
(8, 'marito', 'mariosdd', 'pergolinisss', '223654544', '1984-06-11', 1, 0, NULL, '3211', 'mari@mail.com', '6554544', '', 'Terminal', 2),
(13, 'pacha', 'paolo', 'peña', '32111', NULL, NULL, NULL, NULL, '3211', 'paolo@mail.com', '11666633', '', 'Terminal', 2),
(21, 'perro', 'perro', 'faldero', '221321123', '2001-11-11', 1, 1, 0, '3211', 'perro@mail.com', '1132111', 'Terminal', '0', 3),
(22, 'manco', 'poyo', 'muñolo', '22654', '1987-10-31', 1, 1, 1, '3211', 'manco@mail.com', '11611611', 'Terminal', '0', 3),
(23, 'manolo', 'manolo', 'galvan', '26654654', '1965-06-11', 1, 1, NULL, '3211', 'manolo@mail.com', '1654654', 'Terminal', '0', 3),
(24, 'pancho', 'pancho', 'doto', '221321321', '2001-03-11', 1, 1, 1, '3211', 'mail@pancho.com', '116116161', 'Terminal', '0', 3),
(25, 'flaco', 'roberto', 'spinneta', '221321125', '1998-03-04', 1, 1, 1, '3211', 'spineta@gmail.com', '99999', 'Terminal', '0', 3),
(26, 'viejo', 'robertin', 'castro', '221321152', '1930-10-20', 1, 1, 1, '3211', 'rob@mail.com', '111222333', 'Terminal', '0', 3),
(27, 'roco', 'paolo', 'roca', '221654456', '1925-02-10', 0, 1, 1, '3211', 'paolito@hotmail.com', '5321622', 'Municipal', '0', 3),
(28, 'rafa', 'rafael', 'petroni', '221654456', '1934-01-10', 0, 1, 0, '3211', 'rafa@mail.com', '1162266', 'Terminal', '0', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vacunas`
--

CREATE TABLE `vacunas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `vacunas`
--

INSERT INTO `vacunas` (`id`, `nombre`) VALUES
(5, 'Gripe'),
(6, 'Fiebre amarilla'),
(9, 'Covid');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `turnos`
--
ALTER TABLE `turnos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
--
-- AUTO_INCREMENT de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
