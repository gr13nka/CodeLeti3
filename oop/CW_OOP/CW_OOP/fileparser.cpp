#include "fileparser.h"

FileParser::FileParser()
{
    //std::string Result = FileContent(FileName);
}

std::vector<Event> FileParser::FileContent(std::string FileName)
{
    Error = 0;
    std::ifstream file(FileName);
    if (!file.is_open())
    {
        //std::cout << "Ошибка: файл " << FileName << " не найден\n";
        Error = 1;
        return Events;
    }

    std::stringstream StringStream;
    StringStream << file.rdbuf();
    std::string Content = StringStream.str();


    file.close();

    //std::cout << Content;

    return Events;
}

int FileParser::Check()
{
    return Error;
}
