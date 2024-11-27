#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>
#include <stdlib.h>

#define ledPinRed    0
#define ledPinGreen  1
#define ledPinBlue   2

void setupLedPin(void)
{
	softPwmCreate(ledPinRed,  0, 100);	//Creat SoftPWM pin for red
	softPwmCreate(ledPinGreen,0, 100);  //Creat SoftPWM pin for green
	softPwmCreate(ledPinBlue, 0, 100);  //Creat SoftPWM pin for blue
}

void setLedColor(int r, int g, int b)
{
	softPwmWrite(ledPinRed,   r);	//Set the duty cycle 
	softPwmWrite(ledPinGreen, g);   //Set the duty cycle 
	softPwmWrite(ledPinBlue,  b);   //Set the duty cycle 
}

int main(void)
{
	int r,g,b;
	
	printf("Program is starting ...\n");
	
	wiringPiSetup();	//Initialize wiringPi.
	
	setupLedPin();
	while(1){
		r=random()%100;  //get a random in (0,100)
		g=random()%100;  //get a random in (0,100)
		b=random()%100;  //get a random in (0,100)
		setLedColor(r,g,b);//set random as the duty cycle value 
// If you are using common anode RGBLED,it should be setLedColor(100-r,100-g,100-b) 
// If you want show red, it should be setLedColor(0,100,100)
		printf("r=%d,  g=%d,  b=%d \n",r,g,b);
		delay(1000);
	}
	return 0;
}
