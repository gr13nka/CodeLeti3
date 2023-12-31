format PE console
include '%fasminc%/win32wxp.inc'
entry Start

section '.idata' import readable writeable

library kernel32, 'KERNEL32.DLL', \
        msvcrt,   'MSVCRT.DLL'

import kernel32, ExitProcess, 'ExitProcess',SetFilePointer, 'SetFilePointer',ReadFile,'ReadFile', GetModuleHandleW, 'GetModuleHandleW', CreateFileA, 'CreateFileA',CloseHandle, 'CloseHandle',WriteFile, 'WriteFile'
import msvcrt,printf, 'printf',getch, '_getch', putchar, 'putchar'

section '.data' data readable writeable
Spec db '%d',0
Handle db 0
lpFileName db 'FileName.txt',0
dwDesiredAccess dd GENERIC_WRITE
dwShareMode dd FILE_SHARE_WRITE
lpSecurityAttributes dd 0
dwCreationDisposition dd CREATE_ALWAYS
dwFlagsAndAttributes dd 0
hTemplateFile dd 0
hFile dd 0
;;writefile
lpBuffer db "test", 0
NumberOfBytesToWrite dd 5
;;setfilepointer
FilePointer dd 0
lDistanceToMove dw 0
lpDistanceToMoveHigh dw NULL
dwMoveMethod dw FILE_BEGIN
;;readfile
nNumberOfBytesToRead dw 10
lpNumberOfBytesRead dw NULL
lpOverlapped dw NULL

section '.text' code readable executable
Start:
        invoke CreateFileA, lpFileName, [dwDesiredAccess], [dwShareMode], [lpSecurityAttributes],[dwCreationDisposition], [dwFlagsAndAttributes], [hTemplateFile]
        cmp eax, -1
        je exit
        mov [hFile], eax

        invoke WriteFile, [hFile], lpBuffer,[NumberOfBytesToWrite], NULL, NULL

        invoke SetFilePointer,[hFile], [lDistanceToMove], [lpDistanceToMoveHigh],[dwMoveMethod]
        mov [FilePointer],eax
        invoke ReadFile, [hFile], FilePointer, [lpNumberOfBytesRead],[lpOverlapped]
        cinvoke printf, Spec, eax

        invoke CloseHandle, [hFile]
exit:
        invoke ExitProcess, 0