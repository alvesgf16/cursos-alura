USE vendas_sucos;

SELECT * FROM produtos;

UPDATE produtos
SET
	preco_lista = 5
WHERE
	codigo = '1000889';

UPDATE produtos 
SET 
    embalagem = 'PET',
    tamanho = '1 Litro',
    descritor = 'Sabor da Monstanha - 1 Litro - Uva'
WHERE
    codigo = '1000889';
    
UPDATE produtos
SET
	preco_lista = preco_lista * 1.1
WHERE
	sabor = 'Maracujá';
    
UPDATE clientes 
SET 
    endereco = 'R. Jorge Emílio 23',
    bairro = 'Santo Amaro',
    cidade = 'São Paulo',
    estado = 'SP',
    cep = '8833223'
WHERE
    cpf = '19290992743';