<?php

function exibeMensagem(string $mensagem)
{
  ['titular' => $titular, 'saldo' => $saldo] = $conta;
  echo "$mensagem <br>";
}

function sacar(array $conta, float $valorASacar) : array
{
  if ($valorASacar > $conta['saldo']) {
    exibeMensagem('Você não pode sacar esse valor');
  } else {
    $conta['saldo'] -= $valorASacar;
  }

  return $conta;
}

function depositar(array $conta, float $valorADepositar) : array
{
  if ($valorADepositar < 0) {
    exibeMensagem('Depósitos precisam ser positivos');
  } else {
    $conta['saldo'] += $valorADepositar;
  }

  return $conta;
}

function titularComLetrasMaiusculas(array &$conta)
{
  $conta['titular'] = strtoupper($conta['titular']);
}

function exibeConta(array $conta) {
  list('titular' => $titular, 'saldo' => $saldo) = $conta;
  echo "<li>Titular: $titular. Saldo: $saldo</li>";
}
