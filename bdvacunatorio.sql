-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
<<<<<<< HEAD
-- Tiempo de generación: 16-05-2022 a las 20:54:05
=======
-- Tiempo de generación: 16-06-2022 a las 21:05:14
>>>>>>> master
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

<<<<<<< HEAD
INSERT INTO `turnos` (`id`, `id_usuario`, `fecha_solicitud`, `fecha_turno`, `sede`, `vacuna`, `estado`, `asistio`) VALUES
(102, 99, '2022-05-16', '2022-05-16', 'Cementerio', 'Fiebre amarilla', 2, 1),
(103, 100, '2022-05-16', '2022-05-16', 'Cementerio', 'Gripe', 2, 1),
(104, 102, '2022-05-16', '2022-05-16', 'Cementerio', 'Covid', 2, 1),
(105, 102, '2022-05-16', '2022-06-06', 'Cementerio', 'Covid', 0, 0),
(106, 103, '2022-05-16', '2022-05-16', 'Cementerio', 'Covid', 2, 1),
(108, 103, '2022-05-16', '2022-05-16', 'Cementerio', 'Covid', 2, 1),
(112, 105, '2022-05-16', '2022-06-02', 'Cementerio', 'Gripe', 0, 0);
=======
INSERT INTO `turnos` (`id`, `id_usuario`, `fecha_solicitud`, `fecha_turno`, `sede`, `vacuna`, `numero_dosis`, `estado`, `notificado`, `asistio`, `laboratorio`, `lote`) VALUES
(139, 124, '2022-06-03', '2022-06-04', 'Cementerio', 'Gripe', NULL, 2, NULL, 1, 'Richmond', '1222aaaa'),
(140, 125, '2022-06-03', '2022-06-04', 'Cementerio', 'Fiebre amarilla', NULL, 0, NULL, 1, 'Bagó', '3465'),
(141, 126, '2022-06-03', '2022-06-04', 'Cementerio', 'Covid', 2, 0, NULL, 0, 'Sputnik', '3465546'),
(142, 127, '2022-06-03', '2022-06-04', 'Cementerio', 'Varicela', NULL, 5, NULL, 0, 'Bagó', '546'),
(143, 137, '2022-06-03', '2022-06-04', 'Cementerio', 'Covid', 1, 5, NULL, 0, '', ''),
(144, 138, '2022-06-15', '2022-06-15', 'Cementerio', 'Covid', 1, 2, NULL, 1, 'Sinopharm', '221322'),
(145, 138, '2022-06-15', '2022-06-15', 'Cementerio', 'Covid', 2, 2, NULL, 1, 'Sinopharm', '156555'),
(148, 140, '2022-06-15', '2022-06-15', 'Cementerio', 'Covid', 2, 5, NULL, 0, '', ''),
(149, 140, '2022-06-15', '2022-06-15', 'Cementerio', 'Gripe', 0, 2, NULL, 1, 'Bagó', '8777'),
(150, 138, '2022-06-15', '2022-06-15', 'Cementerio', 'Gripe', 1, 2, NULL, 1, 'Bagó', '122222'),
(151, 141, '2022-06-15', '2022-06-22', 'Cementerio', 'Fiebre amarilla', 1, 0, NULL, 0, '', '');
>>>>>>> master

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
<<<<<<< HEAD
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
=======
(56, 'admin', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'admin', NULL, '12345678', NULL, NULL, 1),
(90, NULL, 'Pedro', 'Gonzalez', '22132111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'pedro@gmail.com', '22222221', NULL, 'Cementerio', 2),
(123, NULL, 'Horacio', 'Gomez', '2213211', '1990-06-10', 0, NULL, NULL, NULL, 0, 0, '3211', 'horacio@gmail.com', '55555555', 'Municipal', '0', 3),
(124, NULL, 'Cristian', 'Pantaleone', '22132111', '1951-07-10', 1, NULL, '2022-06-04', NULL, 0, 0, '3211', 'cristian@gmail.com', '66666666', 'Municipal', '0', 3),
(125, NULL, 'Bruno', 'Zuculini', '22513211', '2001-09-10', 0, NULL, NULL, NULL, 0, 1, '3211', 'naum@gmail.com', '77777777', 'Municipal', '0', 3),
(126, NULL, 'Pity', 'Martinez', '2215636555', '1999-02-11', 0, NULL, '2022-01-22', NULL, 0, 0, '3211', 'pity@gmail.com', '88888888', 'Municipal', '0', 3),
(127, NULL, 'Juan', 'Fernando', '22165454', '2000-02-11', 0, NULL, NULL, NULL, 0, 1, '3211', 'juanfer@gmail.com', '99999999', 'Municipal', '0', 3),
(128, NULL, 'Paulo', 'Ferrari', '22132111', '1995-05-10', 0, NULL, NULL, NULL, 0, 0, '3211', 'paulo@gmail.com', '10000000', 'Cementerio', '0', 3),
(129, NULL, 'Raul', 'Peralta', '22165444', '1950-10-11', 0, '2021-05-10', '2022-06-02', '2022-05-21', 0, 0, '3211', 'rauli@gmail.com', '27154011', 'Cementerio', '0', 3),
(130, NULL, 'sergio', 'De Luca', '22132111', '1979-01-11', 0, '2022-06-02', '2022-06-02', '2022-06-02', 0, 1, '3211', 'sdlbsso@gmail.com', '11111111', 'Cementerio', '0', 3),
(131, NULL, 'Federico', 'Chattas', '221321111', '1940-02-10', 0, '2022-06-02', '2022-06-02', NULL, 0, 0, '3211', 'pepe@gmail.com', '11111112', 'Terminal', '0', 3),
(132, NULL, 'Gustavo', 'Olave', '22132111', '1950-05-14', 1, NULL, NULL, NULL, 0, 0, '3211', 'francis@gmail.com', '1111113', 'Terminal', '0', 3),
(133, NULL, 'Fernando', 'Delarua', '22132111', '1990-02-10', 0, NULL, NULL, NULL, 1, 0, '3211', 'pipi@gmail.com', '11111114', 'Terminal', '0', 3),
(134, NULL, 'federico', 'martin', '22132111', '1950-02-10', 0, '2021-02-11', NULL, NULL, 0, 0, '3211', 'sdlbssoo@gmail.com', '11111199', 'Terminal', '0', 3),
(135, NULL, 'Pablo', 'almada', '2213211188', '2001-02-10', 1, NULL, NULL, NULL, 0, 0, '3212', 'sergio@mail.com', '11111113', 'Terminal', '0', 3),
(136, NULL, 'PEDRO', 'ALARCON', '22132111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '3211', 'pepeala@gmail.com', '22222222', NULL, 'Municipal', 2),
(137, NULL, 'paolo', 'guerrero', '2213211', '1990-02-11', 0, '2022-06-03', '2022-06-03', '2022-06-03', 0, 1, '3211', 'paolo@gmail.com', '12312312', 'Municipal', '0', 3),
(138, NULL, 'mauricio', 'pipo', '2132111', '2000-05-11', 0, '2022-06-15', '2022-06-15', '2022-06-15', 0, 0, '3211', 'mau@hotm.com', '11223344', 'Municipal', '0', 3),
(140, NULL, 'manolo', 'galvan', '22132111', '1940-02-11', 0, NULL, '2022-06-15', NULL, 0, 0, '3211', 'manolo@mail.com.ar', '11223345', 'Municipal', '0', 3),
(141, NULL, 'parco', 'lorca', '22132111', '1990-01-11', 0, NULL, NULL, NULL, 0, 0, '3211', 'parco@gmail.com', '95465444', 'Municipal', '0', 3);
>>>>>>> master

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
<<<<<<< HEAD
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;
=======
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=152;
>>>>>>> master
--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
<<<<<<< HEAD
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;
=======
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=142;
>>>>>>> master
--
-- AUTO_INCREMENT de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
