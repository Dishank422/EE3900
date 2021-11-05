#include<SPI.h>

void setup()
{
	byte rec = 0xff;
	SPIClass SPI1(HSPI);
}

byte spiRead(SPIClass spi) 
{	
	byte received = 0xff;
	spi.beginTransaction();
	digitalWrite(spi.pinSS(), LOW); //pull SS slow to prep other end for transfer
	received = spi.transfer(0xff);
	digitalWrite(spi.pinSS(), HIGH); //pull ss high to signify end of data transfer
	spi.endTransaction();
	return received;
}

void spiWrite(SPIClass spi, byte data) 
{	
	spi.beginTransaction();
	digitalWrite(spi.pinSS(), LOW); //pull SS slow to prep other end for transfer
	spi.transfer(data);
	digitalWrite(spi.pinSS(), HIGH); //pull ss high to signify end of data transfer
	spi.endTransaction();
}

void loop()
{
	rec = spiRead(SPI1);
	if(rec != 0xff)
	{
		spiWrite(SPI1, rec+1);
		rec = 0xff;
	}		
}
