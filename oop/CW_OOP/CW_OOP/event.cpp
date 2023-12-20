#include "event.h"

Event::Event()
{
    //Hittler ZIGA ZAGA
}

Event::Event(int NewType, std::string NewName)
{
    Type = NewType;
    Name = NewName;
}

std::string Event::GetName()
{
    return Name;
}

int Event::GetStart()
{
    return Start;
}

int Event::GetEnd()
{
    return End;
}

void Event::SetStart(int newStart)
{
    Start = newStart;
}

void Event::SetEnd(int newEnd)
{
    End = newEnd;
}
int Event::GetType()
{
    return Type;
}
