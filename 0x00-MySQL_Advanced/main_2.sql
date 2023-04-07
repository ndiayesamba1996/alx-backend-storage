DROP TABLE IF EXISTS `metal_bands`;
CREATE TABLE `metal_bands` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `band_name` varchar(255) DEFAULT NULL,
  `fans` int(11) DEFAULT NULL,
  `formed` year DEFAULT NULL,
  `origin` varchar(255) DEFAULT NULL,
  `split` year DEFAULT NULL,
  `style` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `metal_bands` (`band_name`, `fans`, `formed`, `id`, `origin`, `split`, `style`)
VALUES ('Iron Maiden', '4195', '1975', '1', 'United Kingdom', NULL, 'New wave of british heavy,Heavy'),
('Opeth', '4147', '1990', '2', 'Sweden', '1990', 'Extreme progressive,Progressive rock,Progressive'),
('Metallica', '3712', '1981', '3', 'USA', NULL, 'Heavy,Bay area thrash'),
('Nightwish', '2183', '1996', '10', 'Finland', '1996', 'Symphonic power,Gothic,Symphonic'),
('Alice Cooper', '362', '1964', '257', 'USA', NULL, 'Hard rock,Glam rock,New,Wave ,Heavy'),
('Behemoth', '1721', '1991', '21', 'Poland', NULL, 'Death,Black,Blackened death'),
('Dimmu Borgir', '1688', '1993', '22', 'Norway', '1993', 'Symphonic black,Black'),
('Epica', '1450', '2002', '31', 'The Netherlands', NULL, 'Symphonic'),
('Marilyn Manson', '298', '1989', '303', 'USA', NULL, 'Industrial rock,Alternative,Industrial,Glam rock,Alternative rock'),
('Gojira', '1300', '1996', '38', 'France', '1996', 'Progressive death');
