#ifndef complex_H
#define complex_H

#include <iostream>

using namespace std;
class complex
{
    double re, im;
public:
    complex();
    complex(const int& r);

    complex operator*(complex);
    complex operator+(complex);
    complex operator-(complex);
    complex operator/(complex);

    bool operator>(complex);
    bool operator<(complex);
    bool operator!=(complex);

    friend ostream& operator<<(ostream&,complex);
    friend istream& operator>>(istream&,complex&);
};

#endif // complex_H
