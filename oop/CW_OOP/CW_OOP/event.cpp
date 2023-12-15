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

int Event::GetType()
{
    return Type;
}
