#include <stdio.h>

#include "cai.h"

int main()
{ 
  int a, b, prod, risposta;

  a = cai_extract();
  b = cai_extract();
  prod = a * b;

  printf("Quando fa la seguente moltiplicazione %d * %d?", a, b);
  scanf("%d", &risposta);

  while(risposta =! prod) {
    printf("%s", cai_false());
  }
  printf("%s", cai_true());

  return 0;
}
