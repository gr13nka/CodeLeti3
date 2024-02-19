#include <Windows.h>
#include <stdio.h>
#include <iostream>
//C:\\Windows\\notepad.exe
int main()
{
    setlocale(LC_ALL, "");

    STARTUPINFOA sia;
    PROCESS_INFORMATION pi;

    ZeroMemory(&sia, sizeof(sia));
    ZeroMemory(&pi, sizeof(pi));
    //LP, optional = NULL
    //1 arg = "строка с именем экзе файла" 
    // ret 0 = error, ret !0 = success
    //BOOL bInheritHandles TRUE
    //DWORD dwCreationFlags NORMAL_PRIORITY_CLASS
    int Result = CreateProcessA("C:\\Windows\\notepad.exe", NULL, NULL, NULL, TRUE, NORMAL_PRIORITY_CLASS, NULL, NULL, &sia, &pi);
    if (Result)
        std::cout << "\nSuccess\n";
    else
        std::cout << "\nError\n";
    return 0;
}