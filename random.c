#include <stdlib.h>
#include <time.h>

#include "random.h"

void random_init() {
  srand(time(NULL));
}

int random_moltip(RandomPtr r) {
  r->a = rand() % 11;
  r->b = rand() % 11;
  
  r->risultato = r->a * r->b;
  
  return r->risultato;
}
