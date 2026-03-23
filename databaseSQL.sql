USE BD12022674;
-- 2)
CREATE TABLE IF NOT EXISTS funcionarios(id INT PRIMARY KEY AUTO_INCREMENT,
 nome VARCHAR(100) NOT NULL,
 cargo VARCHAR(50) NOT NULL, 
 salario DECIMAL(10,2) NOT NULL);
 
 -- 3)
 
 ALTER TABLE funcionarios ADD data_admissao DATE NOT NULL;
 
 -- 4)
 
 ALTER TABLE funcionarios DROP COLUMN cargo;
 
 -- 5)
 
 ALTER TABLE funcionarios MODIFY COLUMN salario DECIMAL(12,2);
 
 -- 6)
 
 CREATE TABLE departamentos (id INT PRIMARY KEY AUTO_INCREMENT,
 nome VARCHAR(100) NOT NULL);
 
 ALTER TABLE funcionarios ADD COLUMN departamentoID INT;
 
 ALTER TABLE funcionarios 
 ADD CONSTRAINT FK_departamentoFuncionario 
 FOREIGN KEY (departamentoID) REFERENCES departamentos(id);
 
 -- 7)
 
 ALTER TABLE departamentos ADD COLUMN orcamento DECIMAL(12,2);
 
 -- 8)
 
 ALTER TABLE departamentos DROP COLUMN orcamento;
 
 -- 9)
 
 ALTER TABLE departamentos MODIFY COLUMN nome VARCHAR(150);
 
 -- 10)
 
 ALTER TABLE departamentos RENAME TO setores;
 
 -- 11)
 ALTER TABLE funcionarios DROP CONSTRAINT FK_departamentoFuncionario;
 ALTER TABLE funcionarios DROP COLUMN departamentoID;
 DROP TABLE setores;
 
 -- 12)
 
 ALTER TABLE funcionarios ADD COLUMN status VARCHAR(20) DEFAULT "Ativo";
