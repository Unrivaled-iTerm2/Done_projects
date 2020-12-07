#include <stdio.h>
#include <conio.h>
#include <windows.h>

int life = 3;
char character;

void gotoxy(int x, int y)
{
    COORD Cur;
    Cur.X = x;
    Cur.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), Cur);
}
void print_ground()
{
    printf("  --------\n");
    printf("| |      |\n");
    printf("| | ---  |\n");
    printf("| | |    |\n");
    printf("| | |  --|\n");
    printf("|   |    |\n");
    printf("|---|--  |\n");
    printf("|XXX|    |\n");
    printf("|XXX|--\n");
    printf("----------\n");
    printf("YOUR CHARACTER : %c\n", character);
    printf("LIFE LEFT : %d", life);
}
int Set_color(int text, int back)
{
    CONSOLE_CURSOR_INFO cursor;
    HANDLE handle;
    handle = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(handle, text | back);
    return 0;
}
int main()
{
    printf("Welcome to the mini maze.\nPlease select your character.\nCHARACTER : ");
    scanf("%c", &character);
    int temp;
    int x = 0, y = 0;
    system("mode con: cols=11 lines=11");

    while (true) {
        system("cls");
        print_ground();
        gotoxy(x, y);
        printf("%c", character);
        if ((x >= 2 && y == 0) || (x == 0 && y >= 1) || (x >= 0 && y == 9) || (x == 9 && (y >= 0 && y <= 7)) || (x == 2 && (y >= 0 && y <= 4)) || ((x == 1 || x == 2 || x == 3) && (y >= 6 && y <= 9)) || (x == 4 && y >= 2 && y <= 9) || ((x == 5 || x == 6) && (y == 2 || y == 6 || y == 8)) || ((x == 7 || x == 8) && y == 4))
        {
            --life;
            system("cls");
            print_ground();
            x = 0;
            y = 0;
            gotoxy(0, 0);
            printf("%c", character);
            if (life < 2)
            {
                Set_color(4, 0);
            }
            if (life <= 0)
            {
                printf("-YOU DIED-");
                Sleep(5000);
                return 0;
            }
        }
        if (x == 9 && y == 8)
        {
            goto finish;
        }
        //printf("DEBUG:x:%d, y:%d", x, y);
        temp = _getch();
        if (temp == 100)
        {
            if (x == 10) x = 0;
            else x++;
        }
        else if (temp == 119)
        {
            if (y == 0) y = 10;
            else y--;
        }
        else if (temp == 97)
        {
            if (x == 0) x = 10;
            else x--;
        }
        else if (temp == 115)
        {
            if (y == 10) y = 0;
            else y++;
        }
    }
    {
        finish:
        printf("Yes! you made it!");
        Sleep(5000);
    }
    return 0;
}