(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('inconscienteExplicacionCtlr', function($scope, $experimento) {
    $scope.n_letras = $experimento.inconsciente.n_letras;

    $scope.avanzar = function () {
      this.avanzarDesde('inconsciente-explicacion');
    }.bind($scope);
  });

  parenExperCtlrs.controller('inconscienteExperimentoCtlr', function($scope, $timeout, $experimento, $resultados) {
    $scope.t_prev = $experimento.inconsciente.t_prev;
    $scope.t_expo = $experimento.inconsciente.t_expo;
    $scope.t_resp = $experimento.inconsciente.t_resp;
    $scope.t_buff = $experimento.inconsciente.t_buff;
    $scope.secuencias = $experimento.inconsciente.secuencias;
    $scope.respuestas = $resultados.inconsciente.respuestas;
    $scope.t_prev_letras = $experimento.inconsciente.t_prev_letras;
    $scope.t_expo_letras = $experimento.inconsciente.t_expo_letras;
    $scope.t_resp_letras = $experimento.inconsciente.t_resp_letras;
    $scope.t_buff_letras = $experimento.inconsciente.t_buff_letras;
    $scope.gruposLetras = $experimento.inconsciente.gruposLetras;
    $scope.respuestasLetras = $resultados.inconsciente.respuestasLetras;

    $scope.avanzar = function () {
      this.avanzarDesde('inconsciente-experimento');
    }.bind($scope);

    $scope.$on('tecla-presionada', function(event, args) {
      if (this.preguntaVisible === true && 'charCode' in args) {
        if (args.charCode == 115) {
          this.registrarRespuesta('S');
          $('.boton-si').css("background-color", "lightgreen");
        }
        else if (args.charCode == 110) {
          this.registrarRespuesta('N');
          $('.boton-no').css("background-color", "orange");
        }
      }
      else if (this.preguntaLetraVisible === true && 'charCode' in args) {
        if (args.charCode == 115) {
          this.registrarRespuestaLetra('S');
          $('.boton-si').css("background-color", "lightgreen");
        }
        else if (args.charCode == 110) {
          this.registrarRespuestaLetra('N');
          $('.boton-no').css("background-color", "orange");
        }
      }
    }.bind($scope));

    $scope.preparateVisible = true;
    $scope.secuenciaVisible = false;
    $scope.preguntaVisible = false;
    $scope.letraVisible = false;
    $scope.preguntaLetraVisible = false;
    $scope.promise = null;
    $scope.indiceSecuencias = -1;
    $scope.indiceGruposLetras = -1;
    $scope.letras = null;
    $scope.indiceLetras = -1;
    $scope.timerStart = null;
    $scope.timerEnd = null;
    $scope.timerLetraStart = null;
    $scope.timerLetraEnd = null;

    $scope.ponerProximaSecuencia = function() {
      $('.boton-si').css("background-color", "white");
      $('.boton-no').css("background-color", "white");
      if (this.indiceSecuencias + 1 < this.secuencias.length) {
        this.indiceSecuencias = this.indiceSecuencias + 1;
        this.comenzarExposicion();
      }
      else {
        this.avanzar();
      }
    }.bind($scope);

    $scope.comenzarExposicion = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = true;
      this.preguntaVisible = false;
      this.letraVisible = false;
      this.preguntaLetraVisible = false;
      this.timerStart = (new Date()).getTime();
      this.promise = $timeout(this.empezarTareaAlternativa, this.t_expo(this.secuencias[this.indiceSecuencias]));
    }.bind($scope);

    $scope.terminarExposicion = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = true;
      this.letraVisible = false;
      this.preguntaLetraVisible = false;
      this.promise = $timeout(this.anularRespuesta, this.t_resp);
    }.bind($scope);
    
    $scope.registrarRespuesta = function(respuesta) {
      if (this.preguntaVisible === true) {
          if (this.promise !== null) {
            $timeout.cancel(this.promise);
            this.promise = null;
          }
          this.timerEnd = (new Date()).getTime();
          this.respuestas.push([this.indiceSecuencias, respuesta, this.timerEnd - this.timerStart]);
          this.promise = $timeout(this.ponerProximaSecuencia, this.t_buff);
      }
    }.bind($scope);

    $scope.anularRespuesta = function() {
      if (this.preguntaVisible === true) {
        this.respuestas.push([this.indiceSecuencias, 'X', -1]);
        this.promise = $timeout(this.ponerProximaSecuencia, this.t_buff);
      }
    }.bind($scope);

    $scope.empezarTareaAlternativa = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.letraVisible = false;
      this.preguntaLetraVisible = false;
      this.indiceGruposLetras = (this.indiceGruposLetras + 1) % this.gruposLetras.length;
      this.letras = this.gruposLetras[this.indiceGruposLetras];
      this.indiceLetras = -1;
      this.promise = $timeout(this.ponerProximaLetra, this.t_prev_letras);
    }.bind($scope);

    $scope.ponerProximaLetra = function() {
      $('.boton-si').css("background-color", "white");
      $('.boton-no').css("background-color", "white");
      if (this.indiceLetras + 1 < this.letras.length) {
        this.indiceLetras = this.indiceLetras + 1;
        this.comenzarExposicionLetra();
      }
      else {
        this.preparateVisible = false;
        this.secuenciaVisible = false;
        this.preguntaVisible = false;
        this.letraVisible = false;
        this.preguntaLetraVisible = false;
        this.promise = $timeout(this.terminarExposicion, this.t_buff_letras);
      }
    }.bind($scope);

    $scope.comenzarExposicionLetra = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.letraVisible = true;
      this.preguntaLetraVisible = false;
      this.timerLetraStart = (new Date()).getTime();
      this.promise = $timeout(this.terminarExposicionLetra, this.t_expo_letras);
    }.bind($scope);

    $scope.terminarExposicionLetra = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.letraVisible = false;
      if (this.indiceLetras < 2) {
        this.preguntaLetraVisible = false;
        this.promise = $timeout(this.ponerProximaLetra, 1000);
      }
      else {
        this.preguntaLetraVisible = true;
        this.promise = $timeout(this.anularRespuestaLetra, this.t_resp_letras);
      }
    }.bind($scope);
      
    $scope.registrarRespuestaLetra = function(respuesta) {
      if (this.preguntaLetraVisible === true) {
          if (this.promise !== null) {
            $timeout.cancel(this.promise);
            this.promise = null;
          }
          this.timerLetraEnd = (new Date()).getTime();
          this.respuestasLetras.push([this.indiceGruposLetras, this.indiceLetras, respuesta, this.timerLetraEnd - this.timerLetraStart]);
          this.promise = $timeout(this.ponerProximaLetra, this.t_buff);
      }
    }.bind($scope);

    $scope.anularRespuestaLetra = function() {
      if (this.preguntaLetraVisible === true) {
        this.respuestasLetras.push([this.indiceGruposLetras, this.indiceLetras, 'X', -1]);
        this.promise = $timeout(this.ponerProximaLetra, this.t_buff);
      }
    }.bind($scope);

    $timeout($scope.ponerProximaSecuencia, $scope.t_prev);
  });

})();