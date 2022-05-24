-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 24-05-2022 a las 03:23:55
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
  `fecha_solicitud` date DEFAULT NULL,
  `fecha_turno` date DEFAULT NULL,
  `sede` varchar(50) DEFAULT NULL,
  `vacuna` varchar(50) NOT NULL,
  `estado` int(4) NOT NULL,
  `asistio` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `turnos`
--

INSERT INTO `turnos` (`id`, `id_usuario`, `fecha_solicitud`, `fecha_turno`, `sede`, `vacuna`, `estado`, `asistio`) VALUES
(122, 124, '2022-05-19', '2022-06-18', 'Municipal', 'Gripe', 0, 0),
(124, 127, '2022-05-12', '2022-05-19', 'Cementerio', 'Fiebre amarilla', 2, 1),
(125, 128, '2022-05-19', '2022-06-23', 'Cementerio', 'Fiebre amarilla', 4, 0),
(126, 129, '2022-05-14', '2022-05-21', 'Municipal', 'Covid', 2, 1),
(127, 129, '2022-05-21', '2022-06-20', 'Municipal', 'Gripe', 0, 0);

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
(56, 'admin', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'admin', NULL, NULL, NULL, NULL, 1),
(57, NULL, 'MARIO', 'PANTALEON', '22132111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'marito@gmail.com', '22222223', NULL, 'Municipal', 2),
(58, NULL, 'marisa', 'bali', '221654987', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'mari@mail.com', '22222222', NULL, 'Terminal', 2),
(90, NULL, 'Pedro', 'Gonzalez', '22132111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'pedro@gmail.com', '22222221', NULL, 'Cementerio', 2),
(123, NULL, 'Horacio', 'Gomez', '2213211', '1990-06-10', 0, NULL, NULL, NULL, 0, 0, '3211', 'horacio@gmail.com', '55555555', 'Municipal', '0', 3),
(124, NULL, 'Cristian', 'Pantaleone', '22132111', '1951-07-10', 1, NULL, NULL, NULL, 0, 0, '3211', 'cristian@gmail.com', '66666666', 'Municipal', '0', 3),
(125, NULL, 'Bruno', 'Zuculini', '22513211', '2001-09-10', 0, NULL, NULL, NULL, 0, 1, '3211', 'naum@gmail.com', '77777777', 'Municipal', '0', 3),
(126, NULL, 'Pity', 'Martinez', '2215636555', '1999-02-11', 0, NULL, '2022-01-22', NULL, 0, 0, '3211', 'pity@gmail.com', '88888888', 'Municipal', '0', 3),
(127, NULL, 'Juan', 'Fernando', '22165454', '2000-02-11', 0, NULL, NULL, NULL, 0, 1, '3211', 'juanfer@gmail.com', '99999999', 'Municipal', '0', 3),
(128, NULL, 'Paulo', 'Ferrari', '22132111', '1995-05-10', 0, NULL, NULL, NULL, 0, 0, '3211', 'paulo@gmail.com', '10000000', 'Municipal', '0', 3),
(129, NULL, 'Raul', 'Peralta', '22165444', '1950-10-11', 0, '2021-05-10', NULL, '2022-05-21', 0, 0, '3211', 'rauli@gmail.com', '27154011', 'Municipal', '0', 3);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=128;
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=130;
--
-- AUTO_INCREMENT de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
