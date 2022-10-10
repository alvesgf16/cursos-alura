SELECT 
    *
FROM
    vendedores AS a
        INNER JOIN
    sucos_vendas.tbvendedor AS b ON a.matricula = SUBSTRING(b.MATRICULA, 3, 3);

UPDATE
	vendedores AS a
        INNER JOIN
    sucos_vendas.tbvendedor AS b ON a.matricula = SUBSTRING(b.MATRICULA, 3, 3) 
SET 
    a.ferias = b.DE_FERIAS;


SELECT * FROM clientes;

UPDATE
	clientes AS a
        INNER JOIN
    vendedores AS b ON a.bairro = b.bairro 
SET 
    a.volume_compra = a.volume_compra * 1.3;

SELECT * FROM clientes;