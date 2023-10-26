#include <stdio.h>
#include <string.h>

int isOperation(char *str) {
  if (strlen(str) != 1) {
    return 0;
  }

  int c = str[0];
  return c == '+' || c == '-' || c == '*' || c == '/';
}

int getNumber(char *str) {
  int num = 0;
  int sign = 1;
  for (int i = 0; i < strlen(str); i++) {
    int c = str[i];
    if (c == '-') {
      sign = -1;
      continue;
    }
    num *= 10;
    num += c - '0';
  }

  return num * sign;
}

typedef struct {
  int value[10000];
  int top;
} Stack;

int pop(Stack *s) {
  int res = s->value[s->top];
  s->top--;
  return res;
}

void push(Stack *s, int value) {
  s->top++;
  s->value[s->top] = value;
}

void init(Stack *s) { s->top = -1; }

int evalRPN(char **tokens, int tokensSize) {
  int result = 0;
  char *curr = 0;
  Stack stack;
  int expr1, expr2;

  init(&stack);

  for (int i = 0; i < tokensSize; i++) {
    curr = tokens[i];
    if (!isOperation(curr)) {
      push(&stack, getNumber(curr));
    } else {
      expr2 = pop(&stack);
      expr1 = pop(&stack);
      switch (curr[0]) {
      case '+': {
        push(&stack, expr1 + expr2);
        break;
      }
      case '-': {
        push(&stack, expr1 - expr2);
        break;
      }
      case '*': {
        push(&stack, expr1 * expr2);
        break;
      }
      case '/': {
        // int default to trunc toward zero
        push(&stack, expr1 / expr2);
        break;
      }
      default: {
        printf("Found invalid operator %s", curr);
      }
      }
    }
  }

  result = stack.value[0];
  if (stack.top != 0) {
    printf("Invalid formula!!");
  }

  return result;
}

int main() {
  int res = 0;
  char *s[5];
  // tokens = ["2","1","+","3","*"]

  s[0] = "2";
  s[1] = "1";
  s[2] = "+";
  s[3] = "3";
  s[4] = "*";
  res = evalRPN(s, 5);
  printf("%d\n", res);

  char *s2[13] = {"10","6","9","3","+","-11","*","/","*","17","+","5","+"};
  res = evalRPN(s2, 13);
  printf("%d\n", res);
}
