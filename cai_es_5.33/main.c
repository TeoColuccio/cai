#include <stdio.h>

#include "cai.h"

int main()
{ 
  int a, b, prod, risposta; 
  char scelta = 'n';
  
  cai_init();

  a = cai_extract();
  b = cai_extract();
  prod = a * b;

  do {
  printf("Quando fa la seguente moltiplicazione %d * %d?\n", a, b);
  scanf("%d", &risposta);

  while (risposta != prod) {
    printf("%s\n", cai_false());
    scanf("%d", &risposta);
  }
  printf("%s\n", cai_true());
  
  printf("Vuoi continuare?\n");
  scanf("%s", &scelta);
  } while (scelta == 's');

  return 0;
}
