const int soundPin = 34;   // Analog input pin for sound sensor (AO)
const int buzzerPin = 26;  // Output pin for buzzer

void setup() {
  Serial.begin(115200);
  pinMode(buzzerPin, OUTPUT);
  // pinMode(soundPin, INPUT); // ❌ Not needed — analogRead sets pin mode automatically
}

void loop() {
  int soundValue = analogRead(soundPin);
  Serial.print("Sound Value: ");
  Serial.println(soundValue);

  // Adjust threshold according to your sensor’s noise level
  int threshold = 100; // 🔧 Typical range for ESP32 analog input (0–4095)

  if (soundValue > threshold) {
    digitalWrite(buzzerPin, HIGH);
    Serial.println("DETECT 🔔");
    delay(200); // Short beep
    digitalWrite(buzzerPin, LOW);
    delay(200);
  } else {
    digitalWrite(buzzerPin, LOW); // Ensure buzzer stays off
  }

  delay(100); // Small delay for stability
}