#ifndef MATRIX_H
#define MATRIX_H

#include "number.h"
#include <iostream>

class Matrix
{
private:
        number matrix[3][3];
public:
        void change_matrix();
        void det();
        void transpose(); //by number
        int rang();
        void show_matrix();
};

#endif
