%token BOT
%%
top:BOT;
%%
int yyerror() {return 1;}
int yylex() {return 1;}
