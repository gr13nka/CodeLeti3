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
private:
    std::string TypeName = "default type";
    int Type = 0;
    std::string Name = "default name";
};

#endif // EVENT_H
