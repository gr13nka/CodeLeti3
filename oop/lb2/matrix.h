#ifndef MATRIX_H
#define MATRIX_H

#include "number.h"
#include <iostream>

class Matrix
{
private:
        number matrix[3][3];
public:
        Matrix();
        void change_matrix();
        void det();
        void transpose(); //by number
        void rang();
        void show_matrix();
};

#endif
