#include <Arduino.h>
// C++ code
//

// Farol Principal
int pinVermelho = 10;
int pinAmarelo = 9;
int pinVerde = 8;
int pinBotao = 7;
int pinPedestreVermelho = 3;
int pinPedestreVerde = 2;

int faseSemaforo;

int estadoBotao;
int estadoAnteriorBotao;

void setup() {
  // Semaforo Carros.
  pinMode(pinVermelho, OUTPUT);
  pinMode(pinAmarelo, OUTPUT);
  pinMode(pinVerde, OUTPUT);
  pinMode(pinBotao, INPUT);
  
  //Semaforo Pedrestre.
  pinMode(pinPedestreVermelho, OUTPUT);
  pinMode(pinPedestreVerde, OUTPUT);
  
  // Verifica o Estado do Semaforo.
  faseSemaforo = 1;
  
  // Serve para fazer o botao reconhecer apenas um click caso mantenha ele prescionado.CONTINUA mas ABAQIXO..
  estadoAnteriorBotao = digitalRead(pinBotao);
}


void loop() {
  // Verifica o Botao ligado/Desligado.
  int estadoBotao = digitalRead(pinBotao);
  
  // Verifica se o Botao está ligado/Desligado.
  int ultimoEstadoBotao = estadoBotao;
  
  if ((estadoBotao == HIGH) &&(estadoAnteriorBotao == LOW)) {
    
    if (faseSemaforo < 3) {
      faseSemaforo = faseSemaforo + 1;
  	}else
    	faseSemaforo = 1;
  }
  
  // Serve para fazer o botao reconhecer apenas um click caso mantenha ele prescionado.
  estadoAnteriorBotao = estadoBotao;
  
  // Semaforo esta Verde Aberto.
  if (faseSemaforo == 1) {
  	digitalWrite(pinVerde, HIGH);
    digitalWrite(pinAmarelo, LOW);
    digitalWrite(pinVermelho, LOW);
    
    //Leds Semaforo Pedestre
    digitalWrite(pinPedestreVerde, LOW);
    digitalWrite(pinPedestreVermelho, HIGH);
  }
  
  // Semaforo esta no Amarelo.
  if (faseSemaforo == 2) {
  	digitalWrite(pinVerde, LOW);
    digitalWrite(pinAmarelo, HIGH);
    digitalWrite(pinVermelho, LOW);
    
    //Leds Semaforo Pedestre
    digitalWrite(pinPedestreVerde, LOW);
    digitalWrite(pinPedestreVermelho, HIGH);
  }
  
  // Semaforo esta Vermelho Fechado.
  if (faseSemaforo == 3) {
  	digitalWrite(pinVerde, LOW);
    digitalWrite(pinAmarelo, LOW);
    digitalWrite(pinVermelho, HIGH);
    
    //Leds Semaforo Pedestre
    digitalWrite(pinPedestreVerde, HIGH);
    digitalWrite(pinPedestreVermelho, LOW);
  }
  
  delay(100);
}