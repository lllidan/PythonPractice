#include <iostream>	
#include <math.h>
using namespace std;
int main(int argc, char const *argv[])
{ 
	int open_task(unsigned int task[32],int a,int b);
	unsigned int task[32]= {0};
	int a,b;
	while(scanf("%d,%d",&a,&b)) 
	{
		printf("the task status of %d is %d\n",b,open_task(task,a,b));
	};
	return 0; 
} 
int open_task(unsigned int task[32],int a,int b) 
{ 
	if(a>1024||a<1||b>1024||b<1) return -1;
	void set_task(unsigned int task[32],int a);
	int get_task(unsigned int task[32],int b);
	if(!get_task(task,a)) set_task(task,a);
	if(a==b) return 1; else return get_task(task,b);
 }
 void set_task(unsigned int task[32],int a)
 { 
	int row,column;
	row=(a-1)/32;
	column=(a-1)%32;
	task[row]+=(unsigned int)pow(2,column);
 } 
 int get_task(unsigned int task[32],int b)
 { 
	 int row,column,status,n;
	 unsigned int temp; row=(b-1)/32;
	 column=(b-1)%32;
	 n=0; temp=task[row];
	 do 
	 { 
		 status=temp%2; temp=temp/2;
	 } while((n++)!=column);
	  return status;
 }
