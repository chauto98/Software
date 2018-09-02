#define DEL 8
#define TRA 7
#define IZ 4
#define DER 2
int estado_led_DEL = 0; //cero es apagado
int estado_led_TRA = 0; //cero es apagado
int estado_led_DER = 0; //cero es apagado
int estado_led_IZ = 0; //cero es apagado
int estado_intermitente1 = 0; // intermitente apagado
int estado_intermitente2 = 0; // intermitente apagado
int estado_intermitente3 = 0; // intermitente apagado

void setup() {
  // put your setup code here, to run once:
  pinMode(DEL, OUTPUT);
  pinMode(TRA, OUTPUT);
  pinMode(IZ, OUTPUT);
  pinMode(DER, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  // este if determina que hacer segun el boton apretado
  if (Serial.available() > 0) {
    int lectura = Serial.read();
    if (lectura == '1') {
      prendeDEL();
    }
    else if (lectura == '2') {
      if (estado_led_TRA == 0) {
        estado_led_TRA = 1;
      }
      else {
        estado_led_TRA = 0;
      }
    }
    else if (lectura == '3') {
      if (estado_led_DER == 0) {
        estado_led_DER = 1;
      }
      else {
        estado_led_DER = 0;
      }
    }
    else if (lectura == '4') {
      if (estado_led_IZ == 0) {
        estado_led_IZ = 1;
      }
      else {
        estado_led_IZ = 0;
      }
    }
  } // aca termina el if que revisa el serial
  //--------------------------------------

  //este if decide como se prenden las luces traseras
  if (estado_led_TRA == 0) {
    apagarTRA();
  }
  else {
    prenderTRA();
  }

  // este if decide cómo se prende el intermitente derecho
  if (estado_led_DER == 0) {
    apagarDER();
  }
  else {
    prenderDER();
  }

  // este if decide cómo se prende el intermitente izquierdo
  if (estado_led_IZ == 0) {
    apagarIZ();
  }
  else {
    prenderIZ();
  }

  delay(500);
}

//ve como se prenden las intermitentes del trasero
void prenderTRA() {
  if (estado_intermitente1 == 0) {
    digitalWrite(TRA, HIGH);
    estado_intermitente1 = 1;
  }
  else {
    digitalWrite(TRA, LOW);
    estado_intermitente1 = 0;
  }
}

void apagarTRA() {
  digitalWrite(TRA, LOW);
}

// fija si se prende o apagan las luces delanteras
void prendeDEL() {
  if (estado_led_DEL == 0) {
    digitalWrite(DEL, HIGH);
    estado_led_DEL = 1;
  }
  else {
    digitalWrite(DEL, LOW);
    estado_led_DEL = 0;
  }
  Serial.write("froiz");
}

//ve como se prenden las intermitentes derechas
void prenderDER() {
  if (estado_intermitente2 == 0) {
    digitalWrite(DER, HIGH);
    estado_intermitente2 = 1;
  }
  else {
    digitalWrite(DER, LOW);
    estado_intermitente2 = 0;
  }
}

void apagarDER() {
  digitalWrite(DER, LOW);
}

//ve como se prenden las intermitentes izquierdas
void prenderIZ() {
  if (estado_intermitente3 == 0) {
    digitalWrite(IZ, HIGH);
    estado_intermitente3 = 1;
  }
  else {
    digitalWrite(IZ, LOW);
    estado_intermitente3 = 0;
  }
}

void apagarIZ() {
  digitalWrite(IZ, LOW);
}


