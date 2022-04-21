-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 21-04-2022 a las 02:51:28
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
  `fecha_primera_dosis` date DEFAULT NULL,
  `fecha_ultima_gripe` tinyint(4) DEFAULT NULL,
  `fecha_ultima_covid` tinyint(4) DEFAULT NULL,
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

INSERT INTO `usuarios` (`id`, `usuario`, `nombre`, `apellido`, `telefono`, `nacimiento`, `primera_dosis`, `fecha_primera_dosis`, `fecha_ultima_gripe`, `fecha_ultima_covid`, `paciente_riesgo`, `fiebre_amarilla`, `password`, `email`, `dni`, `sede_preferida`, `sede`, `tipo`) VALUES
(6, 'admin', 'administrador', 'administrador', NULL, NULL, NULL, '0000-00-00', NULL, NULL, NULL, NULL, 'admin', NULL, NULL, '', NULL, 1),
(8, 'marito', 'mariosdd', 'pergolinisss', '223654544', '1984-06-11', 1, '0000-00-00', NULL, NULL, 0, NULL, '3211', 'mari@mail.com', '6554544', '', 'Terminal', 2),
(13, 'pacha', 'paolo', 'peña', '32111', NULL, NULL, '0000-00-00', NULL, NULL, NULL, NULL, '3211', 'paolo@mail.com', '11666633', '', 'Municipal', 2),
(30, 'papaleta', 'patricio', 'lustou', '221321151', NULL, NULL, '0000-00-00', NULL, NULL, NULL, NULL, '3211', 'papa@gmail.com', '1122334455', NULL, 'Municipal', 2);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
--
-- AUTO_INCREMENT de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
