format PE console
include '%fasminc%/win32wxp.inc'
entry Start

section '.idata' import readable writeable

library kernel32, 'KERNEL32.DLL', \
        msvcrt,   'MSVCRT.DLL'

import kernel32, ExitProcess, 'ExitProcess', GetModuleHandleW, 'GetModuleHandleW', CreateFileA, 'CreateFileA',CloseHandle, 'CloseHandle',WriteFile, 'WriteFile'
import msvcrt,printf, 'printf',getch, '_getch', putchar, 'putchar'

section '.data' data readable writeable
Spec db '%c',0
Handle db 0
lpFileName db 'FileName.txt',0
dwDesiredAccess dd GENERIC_WRITE
dwShareMode dd FILE_SHARE_WRITE
lpSecurityAttributes dd 0
dwCreationDisposition dd CREATE_ALWAYS
dwFlagsAndAttributes dd 0
hTemplateFile dd 0
hFile dd 0

lpBuffer dd "hui", 0
NumberOfBytesToWrite dd 3

section '.text' code readable executable

Start:
        invoke CreateFileA, lpFileName, [dwDesiredAccess], [dwShareMode], [lpSecurityAttributes],[dwCreationDisposition], [dwFlagsAndAttributes], [hTemplateFile]
        cmp eax, -1
        je exit
        mov [hFile], eax

        invoke WriteFile, [hFile], lpBuffer,[NumberOfBytesToWrite], NULL, NULL

        invoke CloseHandle, [hFile]
exit:
        invoke ExitProcess, 0