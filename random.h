#ifndef RANDOM_H
#define RANDOM_H

#include <stdio.h>

struct random {
  int a, b, risultato;
};

typedef struct random Random;
typedef struct random* RandomPtr;

void random_init();
int random_moltip();

#endif
