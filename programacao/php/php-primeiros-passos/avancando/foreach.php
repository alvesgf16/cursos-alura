<?php

$contasCorrentes = [
  '123.456.789-10' => [
    'titular' => 'Gabriel',
    'saldo' => 1000
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

$contasCorrentes['132.674.509-10'] = [
  'titular' => 'Cláudia',
  'saldo' => 2000
];

foreach ($contasCorrentes as $cpf => $conta) {
  echo $conta . PHP_EOL;
}