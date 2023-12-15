#include "complex.h"

complex::complex(){}

complex::complex(const int& r)
{
    re = r;
    im = 0;
}

ostream& operator<<(ostream& os,complex c)
{
    os << "(" << c.re << "+" << c.im<< "i)";
    return os;
}

istream& operator>>(istream& is,complex& c)
{
    cout << "enter real part"<< '\n';
    is >> c.re;
    cout << "enter imaginary part"<< '\n';
    is >> c.im;
    return is;
}

complex complex::operator*(complex c)
{
    complex t;
    t.re = c.re*re - c.im*im;
    t.im = c.re*im + c.im*re;
    return t;
}

complex complex::operator/(complex c)
{
    complex t;
    t.re = (re*c.re+im*c.im)/(c.re*c.re+c.im*c.im);
    t.im = (im*c.re-re*c.im)/(c.re*c.re+c.im*c.im);
    return t;
}

complex complex::operator+(complex c)
{
    complex t;
    t.re = c.re + re;
    t.im = c.im + im;
    return t;
}

complex complex::operator-(complex c)
{
    complex t;
    t.re = re - c.re;
    t.im = im - c.im;
    return t;
}


bool complex::operator>(complex c)
{
    if (re>c.re)
        return true;
    else
        return false;
}

bool complex::operator<(complex c)
{
    if (re<c.re)
        return true;
    else
        return false;
}

bool complex::operator!=(complex c)
{
    if (re != c.re || c.im != 0)
        return true;
    else
        return false;
}
