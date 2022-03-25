-- phpMyAdmin SQL Dump
-- version 4.7.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 25-03-2022 a las 04:09:13
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
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `dni` varchar(100) DEFAULT NULL,
  `sede` varchar(100) DEFAULT NULL,
  `tipo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `usuario`, `nombre`, `apellido`, `telefono`, `nacimiento`, `primera_dosis`, `paciente_riesgo`, `password`, `email`, `dni`, `sede`, `tipo`) VALUES
(1, 'kiko', 'federico', 'cuello', '221321321', '2010-05-11', 1, 1, 'kiko', 'f@mail.com', '221321321', '0', 3),
(2, 'mencho', 'ramon', 'medina bello', '22132132115', '2000-09-23', 1, 1, '3211', 'mencho@mail.com', '211321121', '0', 3),
(3, 'pajarito', 'piturro', 'faso', '22332112321', '1930-02-11', 1, 1, '321321', 'vino@gmail.com', '22321123', '0', 3),
(4, 'elio', 'elio', 'correa', '221321564', '1965-06-11', 0, 1, '3211', 'elio@mail.com', '133212222', '0', 3),
(5, 'mario', 'mario', 'bross', '22132115', '2003-06-12', 0, 0, '3211', 'mar@mail.com', '211221', '0', 3),
(6, 'admin', 'administrador', 'administrador', NULL, NULL, NULL, NULL, 'admin', NULL, NULL, NULL, 1),
(7, 'mono', 'mariano', 'moreno', '2215636555', '1964-04-25', 1, 0, '3211', 'mono@mail.com', '19236555', '0', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
