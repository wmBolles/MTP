#include <ncurses.h>
#include <unistd.h>
//#include <string.h>
#include <stdlib.h>
#include <string.h>
#include "Wblib.h"


#define MAX_COMMAND_LENGTH 40
#define MAX_PROCESS_LENGTH 100

typedef struct {
    int x;
    int y;
} Point;

void drawPoint(Point point) {
    mvaddch(point.y, point.x, 'o');
    refresh();
}

void recordProcess(char *process, char *command) {
    strcat(process, command);
    strcat(process, " ");
}

int main(int argc, char *argv[]) {
    initscr();                  
    cbreak();              
    noecho();                 
    keypad(stdscr, TRUE);      
    curs_set(0);         

    int maxX, maxY;
    getmaxyx(stdscr, maxY, maxX);

    Point point = {maxX / 2, maxY / 2};
    drawPoint(point);

    char process[MAX_PROCESS_LENGTH] = "";

    int ch;
    while ((ch = getch()) != 'q') {
        switch (ch) {
            case KEY_RIGHT:
                point.x++;
                break;
            case KEY_LEFT:
                point.x--;
                break;
            case KEY_UP:
                point.y--;
                break;
            case KEY_DOWN:
                point.y++;
                break;
        }

        if (point.x < 0) point.x = 0;
        if (point.x >= maxX) point.x = maxX - 1;
        if (point.y < 0) point.y = 0;
        if (point.y >= maxY) point.y = maxY - 1;

        drawPoint(point);

        if (ch != ERR) {
            char command[MAX_COMMAND_LENGTH];
            if (argc > 1) {
                wB_strcpy(command, argv[1]);
                argc--;
                argv++;
            } else {
                mvprintw(maxY - 1, 0, "Enter a command: ");
                refresh();
                scanw("%s", command);
            }

            if (strcmp(command, "quit") == 0) {
                break;
            } else if (strcmp(command, "left") == 0) {
                point.x--;
            } else if (strcmp(command, "right") == 0) {
                point.x++;
            } else if (strcmp(command, "up") == 0) {
                point.y--;
            } else if (strcmp(command, "down") == 0) {
                point.y++;
            }

            recordProcess(process, command);  // Record the command in the process
        }
    }

    endwin();  // End ncurses

    printf("Process: %s\n", process);  // Print the recorded process

    return 0;
}

