USE vendas_sucos;

INSERT INTO produtos (codigo, descritor, sabor, tamanho, embalagem, preco_lista)
VALUES ('1040107', 'Light - 350 ml - Melancia', 'Melancia', '350 ml', 'Lata', 4.56);

SELECT 
    *
FROM
    produtos;

INSERT INTO produtos (codigo, descritor, sabor, tamanho, embalagem, preco_lista)
VALUES ('1040108', 'Light - 350 ml - Graviola', 'Graviola', '350 ml', 'Lata', 4.00);

INSERT INTO produtos
VALUES ('1040109', 'Light - 350 ml - Açaí', 'Açaí', '350 ml', 'Lata', 5.60);

INSERT INTO produtos
VALUES ('1040110', 'Light - 350 ml - Jaca', 'Jaca', '350 ml', 'Lata', 6.00),
	   ('1040111', 'Light - 350 ml - Manga', 'Manga', '350 ml', 'Lata', 3.50);