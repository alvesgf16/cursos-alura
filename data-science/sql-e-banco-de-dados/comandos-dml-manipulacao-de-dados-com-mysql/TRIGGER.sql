CREATE TABLE faturamento (
    data_venda DATE NULL,
    total_venda FLOAT
);

DELIMITER //
CREATE 
    TRIGGER  tg_calcula_faturamento_insert
 AFTER INSERT ON itens_notas FOR EACH ROW 
    BEGIN
		DELETE FROM faturamento;
		INSERT INTO faturamento
			SELECT 
				a.data_venda,
				SUM(b.quantidade * b.preco) AS total_venda
			FROM
				vendas AS a
					INNER JOIN
				itens_notas AS b ON a.numero = b.numero
			GROUP BY a.data_venda;
    END//

DELIMITER //
CREATE 
    TRIGGER  tg_calcula_faturamento_update
 AFTER UPDATE ON itens_notas FOR EACH ROW 
    BEGIN
		DELETE FROM faturamento;
		INSERT INTO faturamento
			SELECT 
				a.data_venda,
				SUM(b.quantidade * b.preco) AS total_venda
			FROM
				vendas AS a
					INNER JOIN
				itens_notas AS b ON a.numero = b.numero
			GROUP BY a.data_venda;
    END//
    
DELIMITER //
CREATE 
    TRIGGER  tg_calcula_faturamento_delete
 AFTER DELETE ON itens_notas FOR EACH ROW 
    BEGIN
		DELETE FROM faturamento;
		INSERT INTO faturamento
			SELECT 
				a.data_venda,
				SUM(b.quantidade * b.preco) AS total_venda
			FROM
				vendas AS a
					INNER JOIN
				itens_notas AS b ON a.numero = b.numero
			GROUP BY a.data_venda;
    END//

SELECT * FROM clientes;
SELECT * FROM vendedores;

DELETE FROM itens_notas;
DELETE FROM vendas;

INSERT INTO vendas (numero, data_venda, cpf, matricula, imposto)
VALUES ('0100', '2019-05-08', '1471156710', '235', 0.10);
INSERT INTO itens_notas (numero, codigo_produto, quantidade, preco)
VALUES
	('0100', '1000889', 100, 10),
    ('0100', '1002334', 100, 10);

SELECT * FROM vendas;
SELECT * FROM itens_notas;
SELECT * FROM faturamento;

UPDATE itens_notas 
SET 
    quantidade = 200
WHERE
    numero = '0104' AND codigo = '1002334';
    
DELETE FROM itens_notas 
WHERE
    numero = '0104' AND codigo = '1002334';