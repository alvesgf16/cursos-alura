<?php

$peso = 93;
$altura = 1.77;

$imc = peso / altura ** 2;

if ($imc < 18) {
  echo "O IMC está abaixo do recomendado";
} else if ($imc >= 18 && imc <= 25) {
  echo "O IMC está dentro do recomendado";
} else {
  echo "O IMC está acima do recomendado";
}