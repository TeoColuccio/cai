/* Il programma genera 10 moltiplicazioni con tra numeri casuali
 * compresi tra 0 e 10. Lo studente dovrà rispondere ed il programma 
 * calcolerà le risposte esatte, se queste sono inferiori al 75%, il
 * programma consiglia allo studente di ripetere */

#include <stdio.h>

#include "cai.h"

int main()
{ 
  int a, b, prod, risposta, conta = 0, esatte = 0; 
  
  cai_init();

  do {

    a = cai_extract();
    b = cai_extract();
    prod = a * b;

    printf("Quando fa la seguente moltiplicazione %d * %d?\n", a, b);
    scanf("%d", &risposta);

    if (risposta != prod) {
    printf("%s\n", cai_false());
    }
    else {
    printf("%s\n", cai_true());
    esatte++;
    }

    conta++;
  } while (conta < 10);

  if (esatte < 7) {
    printf("\nPlease ask your instructor for extra help!\n");
  }
  else
    printf("Very Good");
  
  return 0;
}
