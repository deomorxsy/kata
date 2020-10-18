```bash
[asari@asari c-probs]$ gcc 1253.c -Wall -Wextra -lm -g -o 1253 
1253.c: In function ‘main’: 
1253.c:4:21: warning: constante caractere muito longa para seu tipo 
    4 |  char alphabet[] = {'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}; 
      |                     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
1253.c:4:21: warning: overflow in conversion from ‘int’ to ‘char’ changes value from ‘1465407834’ to ‘90’ [-Woverflow] 
1253.c:13:13: warning: format ‘%s’ expects argument of type ‘char *’, but argument 3 has type ‘char (*)[51]’ [-Wformat=] 
   13 |  scanf("%d %s %d", &tests, &encoded, &right_shift); 
      |            ~^              ~~~~~~~~ 
      |             |              | 
      |             char *         char (*)[51] 
[asari@asari c-probs]$ gcc 1253.c -Wall -Wextra -lm -g -o 1253 
1253.c: In function ‘main’: 
1253.c:4:21: warning: constante caractere muito longa para seu tipo 
    4 |  char alphabet[] = {'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}; 
      |                     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
1253.c:4:21: warning: overflow in conversion from ‘int’ to ‘char’ changes value from ‘1465407834’ to ‘90’ [-Woverflow] 
1253.c:13:13: warning: format ‘%s’ expects argument of type ‘char *’, but argument 3 has type ‘char (*)[51]’ [-Wformat=] 
   13 |  scanf("%d %s %d", &tests, &encoded, &right_shift); 
      |            ~^              ~~~~~~~~ 
      |             |              | 
      |             char *         char (*)[51] 
1253.c:16:13: warning: format ‘%c’ expects argument of type ‘int’, but argument 2 has type ‘char *’ [-Wformat=] 
   16 |  printf("\n%c\n", alphabet); 
      |            ~^     ~~~~~~~~ 
      |             |     | 
      |             int   char * 
      |            %s 
```

/home/asari/Documentos/coding/exercises/URIOnlineJudge/c-probs

```bash
[asari@asari c-probs]$ gcc 1253.c -Wall -Wextra -lm -g -o 1253 
1253.c: In function ‘main’: 
1253.c:8:17: warning: initialization of ‘char’ from ‘char *’ makes integer from pointer without a cast [-Wint-conversion] 
    8 |  char encoded = "sowat"; 
      |                 ^~~~~~~ 
1253.c:15:29: warning: format ‘%s’ expects argument of type ‘char *’, but argument 3 has type ‘int’ [-Wformat=] 
   15 |  printf("tests=%d\nencoded=%s\nright_shift=%d\n", tests, encoded, right_shift); 
      |                            ~^                            ~~~~~~~ 
      |                             |                            | 
      |                             char *                       int 
      |                            %d 
1253.c:18:30: warning: format ‘%c’ expects argument of type ‘int’, but argument 2 has type ‘char *’ [-Wformat=] 
   18 |  printf("This is alphabet:\n%c\n", alphabet); 
      |                             ~^     ~~~~~~~~ 
      |                              |     | 
      |                              int   char * 
      |                             %s 
```