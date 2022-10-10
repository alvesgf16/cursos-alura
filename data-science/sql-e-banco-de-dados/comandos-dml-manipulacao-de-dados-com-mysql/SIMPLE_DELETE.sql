USE vendas_sucos;

DELETE a FROM notas AS a
INNER JOIN clientes AS b ON a.cpf = b.cpf
WHERE b.idade <= 18;