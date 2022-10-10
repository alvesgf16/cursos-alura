USE vendas_sucos;

CREATE TABLE IF NOT EXISTS produtos (
	codigo VARCHAR(10) NOT NULL,
    descritor VARCHAR(100) NULL,
    sabor VARCHAR(50) NULL,
    tamanho VARCHAR(50) NULL,
    embalagem VARCHAR(50) NULL,
    preco_lista FLOAT NULL,
    PRIMARY KEY (codigo)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS vendedores (
	matricula VARCHAR(5) NOT NULL,
    nome VARCHAR(100) NULL,
    bairro VARCHAR(50) NULL,
    comissao FLOAT NULL,
    data_admissao DATE NULL,
    ferias BIT(1) NULL,
    PRIMARY KEY (matricula)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS clientes (
	cpf VARCHAR(11) NOT NULL,
    nome VARCHAR(100) NULL,
    endereco VARCHAR(150) NULL,
    bairro VARCHAR(50) NULL,
    cidade VARCHAR(50) NULL,
    estado VARCHAR(50) NULL,
    cep VARCHAR(8) NULL,
    data_nascimento DATE NULL,
    idade INTEGER NULL,
    sexo VARCHAR(1) NULL,
    limite_credito FLOAT NULL,
    volume_compra FLOAT NULL,
    primeira_compra BIT(1) NULL,
    PRIMARY KEY (cpf)
) ENGINE=INNODB;

DELIMITER //
CREATE
	TRIGGER tg_clientes_idade_insert
BEFORE INSERT ON clientes FOR EACH ROW
	BEGIN
		SET NEW.idade = timestampdiff(year, NEW.data_nascimento, NOW());
	END//

CREATE TABLE IF NOT EXISTS vendas (
	numero VARCHAR(5) NOT NULL,
    data_venda DATE NULL,
    cpf VARCHAR(11) NOT NULL,
    matricula VARCHAR(5) NOT NULL,
    imposto FLOAT NULL,
    PRIMARY KEY (numero),
    FOREIGN KEY (cpf)
		REFERENCES clientes(cpf)
        ON DELETE CASCADE,
	FOREIGN KEY (matricula)
		REFERENCES vendedores(matricula)
		ON DELETE CASCADE
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS itens_notas (
	numero VARCHAR(5) NOT NULL,
    codigo_produto VARCHAR(10) NOT NULL,
    quantidade INTEGER NULL,
    preco FLOAT NULL,
    PRIMARY KEY (numero, codigo_produto),
    FOREIGN KEY (numero)
		REFERENCES vendas(numero)
        ON DELETE CASCADE,
	FOREIGN KEY (codigo_produto)
		REFERENCES produtos(codigo)
        ON DELETE CASCADE
) ENGINE=INNODB;