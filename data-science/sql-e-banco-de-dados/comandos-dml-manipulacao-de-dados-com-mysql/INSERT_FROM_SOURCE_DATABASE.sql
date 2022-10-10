USE vendas_sucos;

SELECT * FROM sucos_vendas.tbproduto;
SELECT * FROM sucos_vendas.tbcliente;

INSERT INTO produtos
SELECT 
    PRODUTO AS codigo,
    NOME AS descritor,
    SABOR AS sabor,
    TAMANHO AS tamanho,
    EMBALAGEM AS embalagem,
    PRECO_LISTA AS preco_lista
FROM
    sucos_vendas.tbproduto
WHERE
    PRODUTO NOT IN (SELECT 
            codigo
        FROM
            produtos);

INSERT INTO clientes
SELECT
	CPF as cpf,
    NOME as nome,
    CONCAT(ENDERECO1, ' ', ENDERECO2) as endereco,
    BAIRRO as bairro,
    CIDADE as cidade,
    ESTADO as estado,
    CEP as cep,
    DATA_NASCIMENTO as data_nascimento,
    IDADE as idade,
    SEXO as sexo,
    LIMITE_CREDITO as limite_credito,
    VOLUME_COMPRA as volume_compra,
	PRIMEIRA_COMPRA as primeira_compra
FROM sucos_vendas.tbcliente
WHERE CPF NOT IN (SELECT cpf FROM clientes);
        
SELECT * FROM produtos;
SELECT * FROM clientes;
