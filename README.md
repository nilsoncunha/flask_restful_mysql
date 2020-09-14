# # flask_restful
Exemplo de aplicação com a extensão flask-restful utilizando **mysql**

- Executar *app.py* que faz importação do *models.py*
- mysql.py (Arquivo modelo tudo junto)

- Tabelas para teste:

CREATE TABLE `pessoa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `cidade` varchar(45) DEFAULT NULL,
  `idade` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `profissao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome_profissao` varchar(45) NOT NULL,
  `cargo` varchar(45) DEFAULT NULL,
  `id_pessoa` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_profissao_pessoa_idx` (`id_pessoa`),
  CONSTRAINT `fk_profissao_pessoa` FOREIGN KEY (`id_pessoa`) REFERENCES `pessoa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `usuarios` (
  `idusuarios` int NOT NULL AUTO_INCREMENT,
  `login` varchar(20) NOT NULL,
  `senha` varchar(20) NOT NULL,
  PRIMARY KEY (`idusuarios`),
  UNIQUE KEY `login_UNIQUE` (`login`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci