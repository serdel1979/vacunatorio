-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 16-05-2022 a las 20:54:05
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
(102, 99, '2022-05-16', '2022-05-16', 'Cementerio', 'Fiebre amarilla', 2, 1),
(103, 100, '2022-05-16', '2022-05-16', 'Cementerio', 'Gripe', 2, 1),
(104, 102, '2022-05-16', '2022-05-16', 'Cementerio', 'Covid', 2, 1),
(105, 102, '2022-05-16', '2022-06-06', 'Cementerio', 'Covid', 0, 0),
(106, 103, '2022-05-16', '2022-05-16', 'Cementerio', 'Covid', 2, 1),
(108, 103, '2022-05-16', '2022-05-16', 'Cementerio', 'Covid', 2, 1),
(112, 105, '2022-05-16', '2022-06-02', 'Cementerio', 'Gripe', 0, 0);

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
(57, NULL, 'MARIO', 'PANTALEON', '22132111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'marito@gmail.com', '2223', NULL, 'Municipal', 2),
(58, NULL, 'marisa', 'bali', '221654987', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'mari@mail.com', '2222', NULL, 'Terminal', 2),
(90, NULL, 'Pedro', 'Gonzalez', '22132111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'pedro@gmail.com', '2221', NULL, 'Cementerio', 2),
(99, NULL, 'Patricio', 'Lustou', '221654456', '1985-10-10', 0, NULL, NULL, NULL, 0, 1, '3211', 'plusto@gmail.com', '1115', 'Municipal', '0', 3),
(100, NULL, 'Mauricio', 'Macro', '2216544654', '2000-05-20', 0, NULL, '2022-05-16', NULL, 0, 0, '3211', 'mauriciomacro@gmail.com', '1116', 'Municipal', '0', 3),
(101, NULL, 'Federico', 'Pinedo', '2216544654', '1996-03-20', 0, NULL, NULL, NULL, 0, 0, '3211', 'federicopinedo@gmail.com', '1117', 'Municipal', '0', 3),
(102, NULL, 'Juan', 'Piedra', '221563987', '1987-05-20', 0, '2022-05-16', NULL, NULL, 0, 0, '3211', 'juanpiedra@gmail.com', '1118', 'Municipal', '0', 3),
(103, NULL, 'Fernando', 'Severo', '22321321', '1986-05-10', 0, '2022-05-16', NULL, '2022-05-16', 0, 0, '3211', 'severo@gmail.com', '1119', 'Municipal', '0', 3),
(104, NULL, 'Paola', 'Nandez', '221321321', '1990-09-20', 0, NULL, NULL, NULL, 0, 0, '3211', 'paolanandez@gmail.com', '5555', 'Municipal', '0', 3),
(105, NULL, 'Pablo', 'Aimar', '221654987', '1979-08-05', 0, NULL, NULL, NULL, 0, 0, '3211', 'aimar@gmail.com', '1888', 'Municipal', '0', 3),
(106, NULL, 'Guillermo', 'Gatica', '2321321', '2000-06-11', 0, NULL, NULL, NULL, 0, 0, '3211', 'gatica@gmail.com', '1889', 'Municipal', '0', 3);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;
--
-- AUTO_INCREMENT de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
