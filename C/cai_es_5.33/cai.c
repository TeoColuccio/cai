#include <stdio.h>

#include "cai.h"
#include "random.h"

void cai_init()
{
 random_init(); 
}
int cai_extract() 
{
  return random_extract(0, 10);  
}
char* cai_true() 
{
  int rand;

  rand = random_extract(1, 5);

  switch (rand) {
    case 1:
      return "Very good!";
      break;
    case 2:
      return "Excellent!";
      break;
    case 3:
      return "Nice work!";
      break;
    case 4:
      return "Keep up the good work!";
      break;
    }
  return 0;
}

char* cai_false()
{
  int rand;

  rand = random_extract(1, 5);

  switch (rand) {
    case 1: 
      return "No. Please try again.";
      break;
    case 2: 
      return "wrong. Try once more.";
      break;
    case 3:
      return "Don't give up!";
      break;
    case 4:
      return "No. Keep trying.";
      break;
    }
  return 0;
}


