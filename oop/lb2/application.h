#ifndef APPLICATION_H
#define APPLICATION_H

#include <curses.h>
#include <ncurses.h>
#include <iostream>
#include "matrix.h"

class Application
{
public:
    Application();
    void print_menu();
    int run_function(Matrix* m, int selected);
    void exec();
};

#endif
