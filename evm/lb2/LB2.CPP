#include <conio.h>
#include <dos.h>

const char* colname(int color) {
    switch(color) {
        case(0):
                return "CHERNIY";
        case(1):
                return "SINIY";
        case(2):
                return "ZELENIY";
        case(3):
                return "GOLUBOY";
        case(4):
                return "KRASNIY";
        case(5):
                return "MAGNETA";
        case(6):
                return "KORICHNEVIY";
        case(7):
                return "SVETLO-SERIY";
        case(8):
                return "TEMNO-SERIY";
        case(9):
                return "SVETLO-SINIY";
        case(10):
                return "SVETLO-ZELENIY";
        case(11):
                return "SVETLO-GOLUBOY";
        case(12):
                return "SVETLO-KRASNIY";
        case(13):
                return "SVETLO-MAGNETA";
		case(14):
				return "ZHELTIY";
		case(15):
				return "BELIY";
	}
	return 0;
}

void print(int txtcol, int bgcol, int spaces) {
	const char* txtname = colname(txtcol);
	const char* bgname = colname(bgcol);

	//deleting both lines from the top, to perform down scroll
	gotoxy(1, 1);
	for (int i = 0; i <= spaces; i++) {
		delline();
	}

	textattr(bgcol * 16 | txtcol);

	gotoxy(1, 8);
	//when scrolled, add new data to the bottom
	for (int j = 0; j <= spaces; j++) {
		insline();
	}

	cprintf("Text: %s, Background: %s", txtname, bgname);
	return;
}

int main() {
	int x1 = 25, y1 = 8;
	int x2 = 55, y2 = 18;
	int T = 1200;
	int S = 2;
	int max_colors = 16;
	int max_backgrounds = 8;

	textbackground(BLACK);
	textcolor(WHITE);
	clrscr();

	window(x1, y1, x2, y2);

	for (int i = 0; i < max_backgrounds; ++i) {
		for (int j = 0; j < max_colors; ++j)  {
			print(j, i, S);
			if (kbhit())
				return 0;

			delay(T);
		}
	}

	return 0;
}