format PE console
include '%fasminc%/win32wxp.inc'
entry Start

section '.idata' import readable writeable

library kernel32, 'KERNEL32.DLL', \
        msvcrt,   'MSVCRT.DLL'

import kernel32, ExitProcess, 'ExitProcess'

import msvcrt, printf, 'printf',_getch,'_getch'

section '.data' data readable writeable

Hello db 'HeLlo, WorLd!', 0x0D, 0x0A, 0
Spec db '%d', 0

section '.text' code readable executable

Start:
        cinvoke printf, Hello

        stdcall GetStrLen, Hello

        cinvoke printf, Spec, eax
        cinvoke _getch
        invoke ExitProcess, dword 0

proc GetStrLen stdcall uses ecx edi, StrAddr: dword
        mov ecx, [StrAddr]
        xor eax,eax
        dec ecx

count_length:
        inc ecx

        cmp byte [ecx], 0
        je end_count

        cmp  byte [ecx], 'A'
        jb count_length

        cmp  byte [ecx], 'Z'
        ja count_length

        inc eax
        jmp count_length

end_count:
        ret
endp
