CREATE TABLE clientes (
id_cliente INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
cidade VARCHAR(100),
idade INT
);

CREATE TABLE produtos (
id_produto INT AUTO_INCREMENT PRIMARY KEY,
nome_produto VARCHAR(100),
categoria VARCHAR(50),
preco DECIMAL(10,2),
estoque INT
);

INSERT INTO clientes (nome, cidade, idade) VALUES
('Ana Souza', 'Campinas', 25),
('Carlos Lima', 'São Paulo', 40),
('Fernanda Alves', 'Campinas', 32),
('João Pedro', 'Hortolândia', 28),
('Mariana Costa', 'Sumaré', 35),
('Ricardo Gomes', 'Campinas', 45),
('Juliana Rocha', 'São Paulo', 22),
('Bruno Martins', 'Sumaré', 30),
('Patrícia Dias', 'Campinas', 27),
('Lucas Fernandes', 'Hortolândia', 33),
('Camila Ribeiro', 'Campinas', 29),
('Eduardo Silva', 'São Paulo', 50),
('Amanda Freitas', 'Sumaré', 26),
('Felipe Santos', 'Campinas', 38),
('Renata Oliveira', 'Hortolândia', 41);

INSERT INTO produtos (nome_produto, categoria, preco, estoque) VALUES
('Notebook', 'Eletrônicos', 3500.00, 10),
('Mouse', 'Eletrônicos', 80.00, 100),
('Teclado', 'Eletrônicos', 150.00, 80),
('Cadeira', 'Móveis', 600.00, 20),
('Mesa', 'Móveis', 900.00, 15),
('Celular', 'Eletrônicos', 2500.00, 25),
('Fone de ouvido', 'Eletrônicos', 200.00, 50),
('Impressora', 'Eletrônicos', 1200.00, 12),
('Sofá', 'Móveis', 2000.00, 5),
('Luminária', 'Decoração', 120.00, 40),
('Tapete', 'Decoração', 300.00, 30),
('Quadro', 'Decoração', 180.00, 25),
('Monitor', 'Eletrônicos', 1300.00, 18),
('Estante', 'Móveis', 750.00, 10),
('Carregador', 'Eletrônicos', 90.00, 60);

-- 1) Liste todos os dados da tabela clientes
SELECT * from clientes;

-- 2) Liste todos os dados da tabela produtos
SELECT * from produtos;

-- 3) Liste apenas nome e cidade dos clientes
SELECT nome, cidade from clientes;

-- 4) Liste nome_produto e preco dos produtos
SELECT nome_produto, preco from produtos;

-- 5) Liste clientes da cidade “Campinas”
SELECT * FROM clientes WHERE cidade = "Campinas";

-- 6) Liste produtos da categoria “Móveis”
SELECT * FROM produtos WHERE categoria = "Móveis";

-- 7) Liste produtos com preço maior que 500
SELECT * FROM produtos WHERE preco>500;

-- 8) Liste clientes com idade menor que 30
SELECT * FROM clientes WHERE idade<30;

-- 9) Liste clientes de Campinas com idade maior que 30
SELECT * FROM clientes WHERE cidade = "Campinas" AND idade>30;

-- 10) Liste produtos da categoria Eletrônicos com preço maior que 100
SELECT * FROM produtos WHERE categoria = "Eletrônicos" AND preco>100;

-- 11) Liste clientes que moram em Campinas ou São Paulo
SELECT * FROM clientes WHERE cidade = "Campinas" OR cidade = "São Paulo";

-- 12) Liste produtos da categoria Móveis ou Decoração
SELECT * FROM produtos WHERE categoria = "Móveis" OR categoria = "Decoração";

-- 13) Liste clientes cujo nome começa com “A”
SELECT * FROM clientes WHERE nome LIKE "A%";

-- 14) Liste produtos que começam com “C”
SELECT * FROM produtos WHERE nome_produto LIKE "C%";

-- 15) Liste clientes ordenados pelo nome
SELECT * FROM clientes ORDER BY nome;

-- 16) Liste produtos ordenados pelo preço
SELECT * FROM produtos ORDER BY preco;

-- 17) Liste produtos do mais caro para o mais barato
SELECT * FROM produtos ORDER BY preco DESC;

-- 18) Liste clientes do mais velho para o mais novo
SELECT * FROM clientes ORDER BY idade DESC;

-- 19) Conte quantos clientes existem por cidade
SELECT cidade, COUNT(*) AS total FROM clientes GROUP BY cidade;

-- 20) Conte quantos produtos existem por categoria
SELECT categoria, COUNT(*) AS total FROM produtos GROUP BY categoria;

-- 21) Some o valor total dos produtos por categoria
SELECT categoria, SUM(preco) AS total FROM produtos GROUP BY categoria;

-- 22) Calcule a média de preço por categoria
SELECT categoria, AVG(preco) AS media FROM produtos GROUP BY categoria;

-- 23) Mostre cidades com mais de 3 clientes
SELECT cidade, COUNT(*) AS total FROM clientes GROUP BY cidade HAVING COUNT(*) > 3;

-- 24) Mostre categorias com soma de preços maior que 3000
SELECT categoria, SUM(preco) AS total FROM produtos GROUP BY categoria HAVING SUM(preco) > 3000.00;
