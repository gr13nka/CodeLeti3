#include <iostream>
#include <Windows.h>

HANDLE Semaphore;

DWORD WINAPI ThreadFunction1(LPVOID lpParam)
{
    DWORD dwThreadId = GetCurrentThreadId();
   

    while (1) {
        if(WaitForSingleObject(Semaphore, INFINITE) == WAIT_FAILED)
            std::cout << "error waiting Semaphore";
        std::cout << dwThreadId << '\n';
        if (ReleaseSemaphore(Semaphore, 1, NULL) == 0)
            std::cout << "error releasing Semaphore";
    }

    
    return 0;
}

DWORD WINAPI ThreadFunction2(LPVOID lpParam)
{
    DWORD dwThreadId = GetCurrentThreadId();

    while (1) {
        if (WaitForSingleObject(Semaphore, INFINITE) == WAIT_FAILED)
            std::cout << "error waiting Semaphore";
        std::cout << dwThreadId << '\n';
        if (ReleaseSemaphore(Semaphore,1,NULL) == 0)
            std::cout << "error releasing Semaphore";
    }

    return 0;
}

int main()
{
    setlocale(LC_ALL, "");
    HANDLE hThread1;
    HANDLE hThread2;

    Semaphore = CreateSemaphoreA(NULL,1,1,"Egor");
    if (Semaphore == NULL)
    {
        std::cout << "error creating Semaphore";
        return 0;
    }

    DWORD dwThreadId1;
    DWORD dwThreadId2;

    hThread1 = CreateThread(NULL, 0, ThreadFunction1, NULL, 0, &dwThreadId1);
    hThread2 = CreateThread(NULL, 0, ThreadFunction2, NULL, 0, &dwThreadId2);

    if (hThread1 == NULL || hThread2 == NULL)
        std::cout << "error creating a thread";

    if (WaitForSingleObject(hThread2, INFINITE) == WAIT_FAILED || WaitForSingleObject(hThread1, INFINITE) == WAIT_FAILED)
        std::cout << "WaitForSingleObj error";

    if (CloseHandle(hThread1) == false)
        std::cout << "error closing thread1";
    if (CloseHandle(hThread2) == false)
        std::cout << "error closing thread2";
    if (CloseHandle(Semaphore) == false)
        std::cout << "error closing Semaphore";
    
    return 0;
}