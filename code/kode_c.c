#include <stdio.h>

int main() {
  int c, n;

  for (c = 0; c <= 10000; c++) {
    n = rand() % 100 + 1;
    printf("%d\n", n);
  }

  return 0;
}
