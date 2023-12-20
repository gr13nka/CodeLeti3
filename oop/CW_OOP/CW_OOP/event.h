#ifndef EVENT_H
#define EVENT_H

#include <iostream>
#include <QTime>

class Event
{
public:
    Event();
    Event(int NewType, std::string NewName);
    std::string GetName();
    int GetType();
    int GetStart();
    int GetEnd();
    int SetStart();
    int SetEnd(); 
   
private:
    std::string TypeName = "default type";
    int Type = 0;
    int Start;
    int End;
    std::string Name = "default name";
};

#endif // EVENT_H
