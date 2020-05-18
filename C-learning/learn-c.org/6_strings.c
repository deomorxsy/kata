#include <stdio.h>
#include <string.h>

//date: 2020-05-11

int main() {// string types exercise
  char * first_name = "John"; // pointer notation
  char last_name[] = "Doe"; // array notation
  char name[100];

  last_name[0] = 'B';
  sprintf(name, "%s %s", first_name, last_name);

  if (strncmp(name, "John Boe", 100) == 0) {
  	//strncmp compares between two strings, returning
  	//the number 0 if they are equal
      printf("Done!\n");
  }
  name[0]='\0';
  strncat(name,first_name,4);
  strncat(name,last_name,20);
  printf("%s\n",name);
  return 0;
}