#include <stdio.h>

int Bar(){return 1;}
int Fifi(){return 2;}
int Dodo(){return 3;}
int Foo(int a, int b, int c){
return a + b + c;
}
int Gojo(int a, int b){
printf("a: %d\n", a);
printf("b: %d\n", b);
}

int main()
{
//	first line
int i =5;
i = ++i + 1;
printf("i: %d\n" , i);
//	second line
int c,a=2, b =2;
c=(a*b) + (++a + 4);
printf("c: %d\n", c);

//	third line
int g = Foo(Bar(), Fifi(),Dodo());
printf("g: %d\n", g);

//	forth line
int j = 2;
Gojo(++j, j);
printf("j: %d\n", j);
//	fifth line
int m; float f=12.54; f=m=f*2;
printf("m: %d\n f: %f\n", m ,f);

//	sixth line
double d=5; float r=8/6; int t =12; unsigned int ui = 2;
t= d / r + t * (ui - t);
printf("t: %d\n" , t);

}
