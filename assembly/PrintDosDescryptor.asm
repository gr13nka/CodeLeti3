format PE console
include '%fasminc%/win32wxp.inc'
entry Start

section '.idata' import readable writeable

library kernel32, 'KERNEL32.DLL', \
        msvcrt,   'MSVCRT.DLL'

import kernel32, ExitProcess, 'ExitProcess', GetModuleHandleW, 'GetModuleHandleW'
import msvcrt,printf, 'printf',getch, '_getch', putchar, 'putchar'

section '.data' data readable writeable
Spec db '%c',0

section '.text' code readable executable

Start:

       invoke GetModuleHandleW,dword 0
       add eax,4Eh
start:
       mov dl, byte[eax]
       cmp dl, '$'
       je exit
       push eax
       cinvoke printf,Spec,edx
       pop eax
       inc eax
       jmp start
exit:
        invoke ExitProcess, 0