/*
  * threadHello.c -- Simple multi-threaded program.
  *
  * Compile with
  *    > gcc -g -Wall -Werror -D_POSIX_THREAD_SEMANTICS threadHello.c -c -o threadHello.o
  *    > gcc -g -Wall -Werror -D_POSIX_THREAD_SEMANTICS sthread.c -c -o sthread.o
  *    > gcc -lpthread threadHello.o sthread.o -o threadHello
  * Run with
  *    > ./threadHello
  */
#include <stdio.h>
#include <time.h>
#include "sthread.h"

static void go1(int n);
static void go2(int n);

#define NTHREADS 2
static sthread_t threads[NTHREADS];

int main(int argc, char **argv)
{
  int ii;
  struct timespec start, finish;
  double elapsed;


  clock_gettime(CLOCK_MONOTONIC, &start);

  // for(ii = 0; ii < NTHREADS; ii++){
    // sthread_create(&(threads[ii]), &go, ii);
  // }
  sthread_create(&(threads[0]), &go1, 0);
  sthread_create(&(threads[1]), &go2, 1);

  for(ii = 0; ii < NTHREADS; ii++){
    long ret = sthread_join(threads[ii]);
    // printf("Thread %d returned %ld\n", ii, ret);
  }
  clock_gettime(CLOCK_MONOTONIC, &finish);
  printf("Main thread done.\n");

  
  elapsed = (finish.tv_sec - start.tv_sec);
  elapsed += (finish.tv_nsec - start.tv_nsec) / 1000000000.0;
  printf("Total time taken by CPU: %f\n", elapsed);

  return 0;
}

void go1(int n)
{
  // printf("Hello from thread %d\n", n);
  long int count = 0;

  while(1) {
    count++;
    if(count % 10000000 == 0)
      printf(".\n");
  }

  sthread_exit(100 + n);
  // Not reached
}

void go2(int n)
{
  char c;
  while((c = getchar()) != EOF) {
    if(c == '\n')
      printf("Thank you for your input\n");
  }

  sthread_exit(100 + n);
  // Not reached
}
