-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 29-06-2022 a las 19:40:21
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
-- Estructura de tabla para la tabla `laboratorios`
--

CREATE TABLE `laboratorios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `laboratorios`
--

INSERT INTO `laboratorios` (`id`, `nombre`) VALUES
(34, 'ASTRAZENECA'),
(35, 'SPUTNIK'),
(36, 'SINOPHARM'),
(37, 'RICHMOND');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `laboratorio_vacuna`
--

CREATE TABLE `laboratorio_vacuna` (
  `id` int(11) NOT NULL,
  `id_laboratorio` int(11) NOT NULL,
  `id_vacuna` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `laboratorio_vacuna`
--

INSERT INTO `laboratorio_vacuna` (`id`, `id_laboratorio`, `id_vacuna`) VALUES
(117, 37, 6),
(118, 34, 9),
(119, 35, 9),
(120, 36, 9),
(127, 37, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos`
--

CREATE TABLE `turnos` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `fecha_solicitud` date DEFAULT NULL,
  `fecha_turno` date DEFAULT NULL,
  `sede` varchar(50) DEFAULT NULL,
  `vacuna` varchar(50) NOT NULL,
  `numero_dosis` int(11) DEFAULT NULL,
  `estado` int(11) NOT NULL,
  `notificado` tinyint(4) DEFAULT NULL,
  `asistio` tinyint(4) DEFAULT NULL,
  `laboratorio` varchar(50) DEFAULT NULL,
  `lote` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `turnos`
--

INSERT INTO `turnos` (`id`, `id_usuario`, `fecha_solicitud`, `fecha_turno`, `sede`, `vacuna`, `numero_dosis`, `estado`, `notificado`, `asistio`, `laboratorio`, `lote`) VALUES
(181, 163, '2022-06-15', '2022-06-22', 'Municipal', 'Covid', 1, 2, 0, 1, 'SINOPHARM', '988'),
(182, 163, '2022-06-22', '2022-06-29', 'Municipal', 'Gripe', 0, 2, 0, 1, 'RICHMOND', '6555'),
(183, 164, '2022-06-15', '2022-06-22', 'Cementerio', 'Covid', 1, 2, 0, 1, 'SPUTNIK', '232111'),
(184, 164, '2022-06-15', '2022-06-29', 'Cementerio', 'Gripe', 0, 2, 0, 1, 'RICHMOND', '12222'),
(185, 165, '2022-06-15', '2022-06-22', 'Terminal', 'Covid', 1, 2, 0, 1, 'SINOPHARM', '99888'),
(186, 165, '2022-06-22', '2022-06-29', 'Terminal', 'Gripe', 0, 2, 0, 1, 'RICHMOND', '98887'),
(187, 164, '2022-06-29', '2022-07-20', 'Cementerio', 'Covid', 2, 0, 0, 0, '', ''),
(188, 163, '2022-06-29', '2022-07-20', 'Municipal', 'Covid', 2, 0, 0, 0, '', ''),
(189, 165, '2022-06-29', '2022-07-20', 'Terminal', 'Covid', 2, 0, 0, 0, '', ''),
(190, 155, '2022-06-22', '2022-06-29', 'Municipal', 'Gripe', 1, 2, 0, 1, 'RICHMOND', '122111'),
(191, 155, '2022-05-10', '2022-06-22', 'Municipal', 'Covid', 1, 2, 0, 1, 'SINOPHARM', '3322'),
(192, 155, '2022-06-22', '2022-06-29', 'Municipal', 'Covid', 2, 2, 0, 1, 'SPUTNIK', '33333'),
(193, 156, '2022-06-22', '2022-06-29', 'Terminal', 'Gripe', 1, 2, 0, 1, 'RICHMOND', '99999'),
(194, 157, '2022-06-22', '2022-06-29', 'Cementerio', 'Covid', 1, 2, 0, 1, 'SINOPHARM', '6544'),
(195, 157, '2022-06-29', '2022-07-20', 'Cementerio', 'Covid', 2, 0, 0, 0, '', ''),
(196, 158, '2022-06-22', '2022-06-22', 'Municipal', 'Fiebre amarilla', 1, 4, 0, 0, '', ''),
(197, 158, '2022-06-22', '2022-06-29', 'Municipal', 'Gripe', 1, 2, 0, 1, 'RICHMOND', '2222'),
(198, 158, '2022-06-29', '2022-07-11', 'Municipal', 'Covid', 1, 0, 0, 0, '', ''),
(199, 159, '2022-06-22', '2022-06-29', 'Municipal', 'Fiebre amarilla', 1, 2, 0, 1, 'RICHMOND', '112233'),
(200, 159, '2022-06-29', '2022-07-06', 'Municipal', 'Covid', 1, 0, 0, 0, '', ''),
(201, 160, '2022-06-22', '2022-06-29', 'Terminal', 'Fiebre amarilla', 1, 2, 0, 1, 'RICHMOND', '18889'),
(202, 160, '2022-06-29', '2022-07-07', 'Terminal', 'Gripe', 1, 0, 0, 0, '', ''),
(203, 160, '2022-06-29', '2022-07-08', 'Terminal', 'Covid', 1, 0, 0, 0, '', ''),
(204, 161, '2022-06-22', '2022-06-29', 'Terminal', 'Covid', 1, 2, 0, 1, 'SPUTNIK', '1111112222'),
(205, 161, '2022-06-29', '2022-07-07', 'Terminal', 'Fiebre amarilla', 1, 4, 0, 0, '', ''),
(206, 162, '2022-06-29', '2022-07-06', 'Terminal', 'Fiebre amarilla', 1, 0, 0, 0, '', ''),
(207, 162, '2022-06-29', '2022-07-06', 'Terminal', 'Gripe', 1, 0, 0, 0, '', ''),
(208, 162, '2022-06-29', '2022-07-06', 'Terminal', 'Covid', 1, 0, 0, 0, '', ''),
(209, 161, '2022-06-29', '2022-07-20', 'Terminal', 'Covid', 2, 0, 0, 0, '', '');

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
  `fecha_ultima_gripe` date DEFAULT NULL,
  `fecha_ultima_covid` date DEFAULT NULL,
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
(56, 'admin', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'admin', NULL, '12345678', NULL, NULL, 1),
(90, NULL, 'Pedro', 'Gonzalez', '22132111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'pedro@gmail.com', '22222221', NULL, 'Cementerio', 2),
(145, NULL, 'Adolfo', 'Pedernera', '2216565', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'adolfo@gmail.com', '22222222', NULL, 'Municipal', 2),
(146, NULL, 'Homar', 'Sivori', '22132111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'homar@hotmail.com', '22222223', NULL, 'Terminal', 2),
(155, NULL, 'Diego', 'Molina', '2216544', '2014-05-20', 0, '2022-06-29', '2022-06-29', '2022-06-29', 0, 0, '3211', 'diego@gmail.com', '11111111', 'Municipal', '0', 3),
(156, NULL, 'Leonardo', 'Astrada', '22132111', '2010-06-11', 0, NULL, '2022-06-29', NULL, 0, 0, '3211', 'leonardo@gmail.com', '11111112', 'Terminal', '0', 3),
(157, NULL, 'Federico', 'Pipo', '22132111', '2011-03-11', 0, '2022-06-29', NULL, NULL, 0, 0, '3211', 'federico@gmail.com', '11111113', 'Municipal', '0', 3),
(158, NULL, 'Diego', 'Barrado', '22165444', '1995-06-11', 0, NULL, '2022-06-29', NULL, 0, 0, '3211', 'diegobarrado@gmail.com', '11111114', 'Cementerio', '0', 3),
(159, NULL, 'Pablo', 'Fermin', '22132222', '1999-05-20', 0, NULL, NULL, NULL, 0, 1, '3211', 'pablin@gmail.com', '11111115', 'Municipal', '0', 3),
(160, NULL, 'Mauricio', 'Mauri', '2246544', '1985-01-30', 0, NULL, NULL, NULL, 0, 1, '3211', 'mauri@gmail.com', '11111116', 'Cementerio', '0', 3),
(161, NULL, 'Chavo', 'Bianca', '2213211', '1997-05-11', 0, '2022-06-29', NULL, NULL, 0, 0, '3211', 'chavo@gmail.com', '11111117', 'Terminal', '0', 3),
(162, NULL, 'Pipo', 'Gorosito', '6544444', '1994-05-23', 0, NULL, NULL, NULL, 0, 0, '3211', 'pipo@gmail.com', '11111118', 'Terminal', '0', 3),
(163, NULL, 'Ernesto', 'Salomón', '2213211', '1940-10-10', 0, '2022-06-29', '2022-06-29', NULL, 0, 0, '3211', 'ernesti@gmail.com', '11111119', 'Municipal', '0', 3),
(164, NULL, 'Anastacia', 'Luisa', '65445465', '1934-11-15', 0, '2022-06-29', '2022-06-29', NULL, 0, 0, '3211', 'anastacia@hotmail.com', '11111110', 'Cementerio', '0', 3),
(165, NULL, 'Joaquin', 'Pineda', '2232111', '1933-06-11', 0, '2022-06-29', '2022-06-29', NULL, 0, 0, '3211', 'joaquin@gmail.com', '11111120', 'Terminal', '0', 3);

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
-- Indices de la tabla `laboratorios`
--
ALTER TABLE `laboratorios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `laboratorio_vacuna`
--
ALTER TABLE `laboratorio_vacuna`
  ADD PRIMARY KEY (`id`);

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
-- AUTO_INCREMENT de la tabla `laboratorios`
--
ALTER TABLE `laboratorios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;
--
-- AUTO_INCREMENT de la tabla `laboratorio_vacuna`
--
ALTER TABLE `laboratorio_vacuna`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=129;
--
-- AUTO_INCREMENT de la tabla `turnos`
--
ALTER TABLE `turnos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=210;
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=166;
--
-- AUTO_INCREMENT de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
