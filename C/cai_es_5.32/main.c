#include <stdio.h>

#include "cai.h"

int main()
{ 
  int a, b, prod, risposta;
  
  cai_init();

  a = cai_extract();
  b = cai_extract();
  prod = a * b;

  printf("Quando fa la seguente moltiplicazione %d * %d?\n", a, b);
  scanf("%d", &risposta);

  while (risposta != prod) {
    printf("%s\n", cai_false());
    scanf("%d", &risposta);
  }
  printf("%s\n", cai_true());

  return 0;
}
