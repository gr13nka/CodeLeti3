#include <iostream>
#include <Windows.h>
#include <tlhelp32.h>
#include <tchar.h>

int main()
{
	setlocale(LC_ALL, "");
	HANDLE hThread1;
	PROCESSENTRY32 pi;

	hThread1 = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	if (hThread1 == INVALID_HANDLE_VALUE)
		std::cout << "error creating";

	ZeroMemory(&pi, sizeof(pi));
	pi.dwSize = sizeof(pi);
	
	if (Process32First(hThread1, &pi) == false)
		std::cout << "error proccesinging";


	bool flag = true;
	while (flag)
	{
		ZeroMemory(&pi, sizeof(pi));
		pi.dwSize = sizeof(pi);
		flag = Process32Next(hThread1, &pi);
		_tprintf(TEXT("%s\n"), pi.szExeFile);
	}

	if (CloseHandle(hThread1) == FALSE)
		printf("Error closing\n");
	
	return 0;
}