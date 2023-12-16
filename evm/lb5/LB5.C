#include <stdio.h>
#include <dos.h>
#include <stdlib.h>

#define INTR 0x08

const int TactsPerSecond = 18; //this is amount specified in inter
int SecondsAmount = 3;
volatile int Counter = 0;  //volatile so compiler will not modify or hide it
volatile int TacktsANDSecAmount = 0;

void interrupt far (*old_interrupt_handler)(void);

void interrupt new_interrupt_handler(void)
{
	Counter++;

	(*old_interrupt_handler)();
}

int main()
{
	int Succes,tmp = 0;
	old_interrupt_handler = _dos_getvect(INTR);
	_dos_setvect(INTR, new_interrupt_handler);
	clrscr();
	randomize();
	SecondsAmount = rand()%10;
	TacktsANDSecAmount = TactsPerSecond * SecondsAmount;

	while(1)
	{

		if (Counter >= TacktsANDSecAmount)
		{
			Succes = 1;
			break;
		}

		if (kbhit())
			break;

		if (Counter / TactsPerSecond != tmp)
		{
			tmp = Counter / TactsPerSecond;
			printf(" %d", tmp);
		}
	}

	if (Succes)
	{
		sound(500);
		delay(2000);
		nosound();
	}

	getch();

	_dos_setvect(INTR, old_interrupt_handler);
	return 0;
}