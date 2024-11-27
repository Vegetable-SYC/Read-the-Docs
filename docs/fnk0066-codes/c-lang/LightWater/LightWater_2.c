while(1){
	for(i=0;i<ledCounts;i++){   // move led(on) from left to right
		digitalWrite(pins[i],LOW);
		delay(100);
		digitalWrite(pins[i],HIGH);
	}
	for(i=ledCounts-1;i>-1;i--){   // move led(on) from right to left
		digitalWrite(pins[i],LOW);
		delay(100);
		digitalWrite(pins[i],HIGH);
	}
}
