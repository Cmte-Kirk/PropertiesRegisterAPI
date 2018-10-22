-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: 22-Out-2018 às 21:25
-- Versão do servidor: 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `imoveis`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `imobiliaria`
--

DROP TABLE IF EXISTS `imobiliaria`;
CREATE TABLE IF NOT EXISTS `imobiliaria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `endereco` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `imobiliaria`
--

INSERT INTO `imobiliaria` (`id`, `nome`, `endereco`) VALUES
(1, 'Imobiliaria 1', 'rua da imobiliaria 1'),
(2, 'Imobiliária mais 2', 'rua da imobiliaria 2'),
(4, 'Imobiliaria 4', 'rua da imobiliaria 4');

-- --------------------------------------------------------

--
-- Estrutura da tabela `imovel`
--

DROP TABLE IF EXISTS `imovel`;
CREATE TABLE IF NOT EXISTS `imovel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `endereco` varchar(250) NOT NULL,
  `descricao` varchar(250) NOT NULL,
  `status` enum('Ativo','Inativo') NOT NULL,
  `caracteristicas` varchar(500) DEFAULT NULL,
  `tipo` enum('Apartamento','Casa') NOT NULL,
  `finalidade` enum('Residencial','Escritório') DEFAULT NULL,
  `idimobiliaria` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_IMOVEL_IMOBILIARIA_idx` (`idimobiliaria`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `imovel`
--

INSERT INTO `imovel` (`id`, `nome`, `endereco`, `descricao`, `status`, `caracteristicas`, `tipo`, `finalidade`, `idimobiliaria`) VALUES
(1, 'nome teste', 'rua teste', 'desc teste', 'Ativo', '', 'Casa', NULL, 1),
(2, 'Imovel teste 2', 'rua teste 2', 'desc teste', 'Inativo', 'Caracteristicas de teste', 'Casa', 'Residencial', 2);

--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `imovel`
--
ALTER TABLE `imovel`
  ADD CONSTRAINT `FK_IMOVEL_IMOBILIARIA` FOREIGN KEY (`idimobiliaria`) REFERENCES `imobiliaria` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
