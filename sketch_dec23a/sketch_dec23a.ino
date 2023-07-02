#include <DHT.h>
#define DHTPIN 5
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  String output = "mills,";
  output += String(millis());
  output += ",available,";
  output += String(dht.read());
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  output += ",humidity,";
  if (isnan(h)) {
    output += "NAN";
  } else {
    output += h;
  }
  output += ",temp,";
  if (isnan(t)) {
    output += "NAN";
  } else {
    output += t;
  }
  output += ";\n";
  
  Serial.print(output);
}
