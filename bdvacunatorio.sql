-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 25-06-2022 a las 01:56:01
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
(37, 'RICHMOND'),
(38, 'BAGÓ');

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
(115, 37, 5),
(116, 38, 5),
(117, 37, 6),
(118, 34, 9),
(119, 35, 9),
(120, 36, 9);

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
(160, 147, '2022-05-24', '2022-07-05', 'Cementerio', 'Fiebre amarilla', 1, 0, 0, 0, '', ''),
(161, 147, '2022-05-20', '2022-07-01', 'Cementerio', 'Gripe', 1, 2, 0, 1, 'RICHMOND', '122222'),
(162, 148, '2022-04-24', '2022-07-05', 'Terminal', 'Covid', 1, 0, 0, 0, '', ''),
(163, 148, '2022-05-24', '2022-07-10', 'Terminal', 'Fiebre amarilla', 1, 0, 0, 0, '', ''),
(164, 148, '2022-06-20', '2022-07-15', 'Municipal', 'Gripe', 1, 0, 0, 0, '', ''),
(165, 149, '2022-06-10', '2022-06-24', 'Cementerio', 'Covid', 1, 2, 0, 1, 'SPUTNIK', '5467547'),
(166, 149, '2022-06-10', '2022-06-24', 'Cementerio', 'Gripe', 1, 5, 0, 0, '', ''),
(167, 149, '2022-06-24', '2022-07-15', 'Cementerio', 'Covid', 2, 0, 0, 0, '', ''),
(168, 150, '2022-06-24', '2022-07-05', 'Terminal', 'Covid', 1, 0, 1, 0, '', ''),
(169, 150, '2022-06-24', '2022-07-19', 'Cementerio', 'Fiebre amarilla', 1, 4, 0, 0, '', ''),
(170, 151, '2022-06-01', '2022-06-24', 'Municipal', 'Covid', 1, 2, 0, 1, 'SINOPHARM', '4455555'),
(171, 151, '2022-06-24', '2022-07-15', 'Municipal', 'Covid', 2, 0, 0, 0, '', ''),
(177, 154, '2022-05-04', '2022-06-15', 'Municipal', 'Covid', 1, 2, 0, 1, 'SPUTNIK', '12122'),
(178, 154, '2022-06-15', '2022-06-24', 'Municipal', 'Gripe', 0, 2, 0, 1, 'BAGÓ', '6555'),
(179, 154, '2022-06-24', '2022-07-15', 'Municipal', 'Covid', 2, 0, 0, 0, '', '');

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
(147, NULL, 'Enzo', 'Pérez', '22132111', '1982-01-11', 0, NULL, '2022-06-24', NULL, 0, 0, '3211', 'sdlbsso@gmail.com', '27154011', 'Municipal', '0', 3),
(148, NULL, 'Mario', 'Mordini', '22132111', '1990-05-20', 0, NULL, NULL, NULL, 0, 0, '3211', 'marito@gmail.com', '11111111', 'Terminal', '0', 3),
(149, NULL, 'Franco', 'Armani', '22165444', '2000-05-11', 0, '2022-06-24', NULL, NULL, 0, 0, '3211', 'franco@mail.com.ar', '11111112', 'Municipal', '0', 3),
(150, NULL, 'Juana', 'De Luca', '221321111', '2010-12-11', 0, NULL, NULL, NULL, 0, 0, '3211', 'jujuanitacobanera@gmail.com', '50268750', 'Municipal', '0', 3),
(151, NULL, 'Danila', 'Cagliardo', '22132111', '1996-09-11', 0, '2022-06-24', NULL, NULL, 0, 0, '3211', 'danila@gmail.com', '11111113', 'Municipal', '0', 3),
(154, NULL, 'Lola', 'Mora', '1121213211', '1940-05-11', 0, '2022-06-24', '2022-06-24', NULL, 0, 0, '3211', 'lol@mail.com', '11111115', 'Municipal', '0', 3);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
--
-- AUTO_INCREMENT de la tabla `laboratorio_vacuna`
--
ALTER TABLE `laboratorio_vacuna`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;
--
-- AUTO_INCREMENT de la tabla `turnos`
--
ALTER TABLE `turnos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=180;
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=155;
--
-- AUTO_INCREMENT de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
