#include "application.h"
#include "matrix.h"

const char* choices[]
{
    "1. input 3x3 matrix row by row",
    "2. show matrix",
    "3. count matrix determinant",
    "4. transpose matrix",
    "5. count matrix rang",
    "6. exit"
};
int n_choices = sizeof(choices) / sizeof(char *);

void Application::print_menu()
{
    for (int i = 0; i < n_choices; ++i)
    {
       /*if (choice == i)
        {
            printf("%s%s%c", choices[i], " ",'\n');
        }
        else
        */
            printf("%s%c", choices[i], '\n');
    }
}

int Application::run_function(Matrix* m, int selected)
{

/*
    "input 3x3 matrix row by row",
    "show matrix",
    "count matrix determinant",
    "transpose matrix",
    "count matrix rang",
        */
    switch (selected) {

        case 1:
            m->change_matrix();
            return 0;
        case 2:
            m->show_matrix();
            return 0;
        case 3:
            m->det();
            return 0;
        case 4:
            m->transpose();
            return 0;
        case 5:
            m->rang();
            return 0;
        case 6:
            return 1;
    }
    return 1;
}

Application::Application(){}

void Application::exec()
{
    int key,stop;
    Matrix m;

    while (true)
    {
        print_menu();
        std::cin >> key;

        stop = run_function(&m,key);

        if(stop == 1)
            return;
    }
    return;
}
