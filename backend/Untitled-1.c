/*
 * Main source code file for lsh shell program
 *
 * You are free to add functions to this file.
 * If you want to add functions in a separate file(s)
 * you will need to modify the CMakeLists.txt to compile
 * your additional file(s).
 *
 * Add appropriate comments in your code to make it
 * easier for us while grading your assignment.
 *
 * Using assert statements in your code is a great way to catch errors early and make debugging easier.
 * Think of them as mini self-checks that ensure your program behaves as expected.
 * By setting up these guardrails, you're creating a more robust and maintainable solution.
 * So go ahead, sprinkle some asserts in your code; they're your friends in disguise!
 *
 * All the best!
 */
#include <assert.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <readline/readline.h>
#include <readline/history.h>

// The <unistd.h> header is your gateway to the OS's process management facilities.
#include <unistd.h>

#include "parse.h"
// to fork processes
#include <sys/wait.h>
#include <sys/types.h>

static void print_cmd(Command *cmd);
static void print_pgm(Pgm *p);
void stripwhite(char *);
void run_commands(char *line);
void run_commands_generalized(char *line, char *cmd);

int main(void)
{
  for (;;)
  {
    char *line;
    line = readline("> ");

    //Ctrl-D Handling
    if(line == NULL)
    {
      exit(0);
    }


    // Remove leading and trailing whitespace from the line
    stripwhite(line);

    if (*line)
    {
      add_history(line);

      Command cmd;
      if (parse(line, &cmd) == 1)
      {

        run_commands(line);
        // run_commands_generalized(line, &cmd);
        // Just prints cmd
        print_cmd(&cmd);
      }
      else
      {
        printf("Parse ERROR\n");
      }
    }

    // Clear memory
    free(line);
  }

  return 0;
}

/*
 * Print a Command structure as returned by parse on stdout.
 *
 * Helper function, no need to change. Might be useful to study as inspiration.
 */
static void print_cmd(Command *cmd_list)
{
  printf("------------------------------\n");
  printf("Parse OK\n");
  printf("stdin:      %s\n", cmd_list->rstdin ? cmd_list->rstdin : "<none>");
  printf("stdout:     %s\n", cmd_list->rstdout ? cmd_list->rstdout : "<none>");
  printf("background: %s\n", cmd_list->background ? "true" : "false");
  printf("Pgms:\n");
  print_pgm(cmd_list->pgm);
  printf("------------------------------\n");
}

/* Print a (linked) list of Pgm:s.
 *
 * Helper function, no need to change. Might be useful to study as inpsiration.
 */
static void print_pgm(Pgm *p)
{
  if (p == NULL)
  {
    return;
  }
  else
  {
    char **pl = p->pgmlist;

    /* The list is in reversed order so print
     * it reversed to get right
     */
    print_pgm(p->next);
    printf("            * [ ");
    while (*pl)
    {
      printf("%s ", *pl++);
    }
    printf("]\n");
  }
}


/* Strip whitespace from the start and end of a string.
 *
 * Helper function, no need to change.
 */
void stripwhite(char *string)
{
  size_t i = 0;

  while (isspace(string[i]))
  {
    i++;
  }

  if (i)
  {
    memmove(string, string + i, strlen(string + i) + 1);
  }

  i = strlen(string) - 1;
  while (i > 0 && isspace(string[i]))
  {
    i--;
  }

  string[++i] = '\0';
}

void run_commands(char *line){
  pid_t pid = fork();
    //child process
    if (pid == 0)
    {
      // char *const argv[] = {"ls", "date", "who", NULL};
      if (strcmp(line, "ls") == 0)
      {
        char *const argv[] = {"ls", NULL};
        execvp("ls", argv);
      }
      else if (strcmp(line, "date") == 0)
      {
        char *const argv[] = {"date", NULL};
        execvp("date", argv);
      }
      else if (strcmp(line, "who") == 0)
      {
        char *const argv[] = {"who", NULL};
        execvp("who", argv);
      }
      else
      {
        printf("Unknown command\n");
      }
      exit(0);
    }
    // fork failed
    else if (pid < 0)
    {
      perror("Fork failed");
    }
    //parent process
    else
    {
      wait(NULL);
    }
}

void run_commands_generalized(char *line, Command *cmd){
  pid_t pid = fork();
    //child process

    if (pid == 0)
    {
      char *argv[128]; //holds the command, 128 is temporary
      int i = 0;
      int status;
      Pgm *pg = cmd.pgm;
      execvp(pg->pgmlist[0], pg->pgmlist);

      if(1){ //execute the path
        
        exit(0);
      }

      // if failes 
      exit(1);
    }
    // fork failed
    else if (pid < 0)
    {
      perror("Fork failed");
    }
    //parent process
    else
    {   
        // Background
        if (cmd.background == 1){
            waitpid(pid,&status,WNOHANG);
        }
        else{ // Foreground
            waitpid(pid,&status,0);
        }

    }
}