format PE console
include '%fasminc%/win32wxp.inc'
entry Start

section '.idata' import readable writeable

library kernel32, 'KERNEL32.DLL', \
        msvcrt,   'MSVCRT.DLL'

import kernel32, ExitProcess, 'ExitProcess',VirtualAlloc,'VirtualAlloc',VirtualFree,'VirtualFree'
import msvcrt,printf, 'printf',getch, '_getch', putchar, 'putchar',scanf,'scanf'

section '.data' data readable writeable
Spec db '%s',0
Handle db 0
lpFileName db 'FileName.txt',0
dwDesiredAccess dd GENERIC_WRITE
dwShareMode dd FILE_SHARE_WRITE
lpSecurityAttributes dd 0
dwCreationDisposition dd CREATE_ALWAYS
dwFlagsAndAttributes dd 0
hTemplateFile dd 0
hFile dd 0
;; writefile
lpBuffer db "test", 0
NumberOfBytesToWrite dd 5
;; setfilepointer
FilePointer dd 0
lDistanceToMove dw 0
lpDistanceToMoveHigh dw NULL
dwMoveMethod dw FILE_BEGIN
;; readfile
nNumberOfBytesToRead dw 10
lpNumberOfBytesRead dw NULL
lpOverlapped dw NULL
;; Alloc
Buffer dd 0
lpAddress dw NULL
dwSize dw 10
flAllocationType dw MEM_COMMIT
flProtect dw PAGE_READWRITE
;; Free
dwFreeType dw MEM_RELEASE
section '.text' code readable executable
Start:
        invoke VirtualAlloc, dword 0, dword 100, dword MEM_COMMIT ,dword  PAGE_READWRITE
        mov [Buffer], eax
        cmp eax, NULL
        je exit

        cinvoke scanf, Spec, [Buffer]
        cinvoke printf, Spec, [Buffer]

        invoke VirtualFree,[Buffer],dword 0,dword MEM_RELEASE
        cmp eax,0
        je error
exit:
        invoke ExitProcess, 0
error:
        cinvoke printf, Spec,"Free Error"
        cinvoke getch
        jmp exit