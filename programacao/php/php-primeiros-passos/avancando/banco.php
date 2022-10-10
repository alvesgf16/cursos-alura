<?php

require_once 'funcoes.php';

$contasCorrentes = [
  '123.456.789-10' => [
    'titular' => 'Gabriel',
    'saldo' => 100
  ],
  '123.454.789-11' => [
    'titular' => 'Maria',
    'saldo' => 10000
  ],
  '123.256.789-10' => [
    'titular' => 'Alberto',
    'saldo' => 300
  ]
];

$contasCorrentes['123.454.789-11'] = sacar($contasCorrentes['123.454.789-11'], 500);
$contasCorrentes['123.256.789-10'] = sacar($contasCorrentes['123.256.789-10'], 200);
$contasCorrentes['123.456.789-10'] = depositar($contasCorrentes['123.456.789-10'], 900);

unset($contasCorrentes['123.256.789-10']);

titularComLetrasMaiusculas($contasCorrentes['123.456.789-10']);

foreach ($contasCorrentes as $cpf => $conta) {
  exibeConta($conta);
}


