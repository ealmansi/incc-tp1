(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('inconscienteExplicacionCtlr', function($scope, $experimento) {
    $scope.t_expo = $experimento.inconsciente.t_expo;
    $scope.t_resp = $experimento.inconsciente.t_resp;
    $scope.n_letras = $experimento.inconsciente.n_letras;

    $scope.avanzar = function () {
      this.avanzarDesde('inconsciente-explicacion');
    }.bind($scope);
  });

  parenExperCtlrs.controller('MenuCtrl', function () {});
  parenExperCtlrs.directive('focusIf', [function () {
      return function focusIf(scope, element, attr) {
          scope.$watch(attr.focusIf, function (newVal) {
              if (newVal) {
                  element[0].focus();
                  // You can write element.focus() if jQuery is available
              }
          });
      }
  }]);

  parenExperCtlrs.controller('inconscienteExperimentoCtlr', function($scope, $timeout, $experimento, $resultados) {
    $scope.t_prev = $experimento.inconsciente.t_prev;
    $scope.t_expo = $experimento.inconsciente.t_expo;
    $scope.t_resp = $experimento.inconsciente.t_resp;
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

    $scope.ponerProximaSecuencia = function() {
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
      this.promise = $timeout(this.empezarTareaAlternativa, this.t_expo);
    }.bind($scope);

    $scope.terminarExposicion = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = true;
      this.letraVisible = false;
      this.preguntaLetraVisible = false;
      this.promise = $timeout(this.anularRespuesta, this.t_resp);
    }.bind($scope);
    
    $scope.registrarRespuesta = function(keyCode) {
      if(keyCode===78){
        respuesta = "No";
      }
      else if (keyCode === 83)
      {
        respuesta = "Si";
      }
      else {
        respuesta = "X";
      }
      if (this.preguntaVisible === true) {
          if (this.promise !== null) {
            $timeout.cancel(this.promise);
            this.promise = null;
          }
          this.respuestas.push([this.indiceSecuencias, respuesta]);
          this.ponerProximaSecuencia();
      }
    }.bind($scope);

    $scope.anularRespuesta = function() {
      if (this.preguntaVisible === true) {
        this.respuestas.push([this.indiceSecuencias, 'X']);
        this.ponerProximaSecuencia();
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
      this.promise = $timeout(this.terminarExposicionLetra, this.t_expo_letras);
    }.bind($scope);

    $scope.terminarExposicionLetra = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.letraVisible = false;
      if (this.indiceLetras < 2) {
        this.preguntaLetraVisible = false;
        this.promise = $timeout(this.ponerProximaLetra, this.t_resp_letras / 2);
      }
      else {
        this.preguntaLetraVisible = true;
        this.promise = $timeout(this.anularRespuestaLetra, this.t_resp_letras);
      }
    }.bind($scope);
      
    $scope.registrarRespuestaLetra = function(keyCode) {
      if(keyCode===78){
        respuesta = "No";
      }
      else if (keyCode === 83)
      {
        respuesta = "Si";
      }
      else {
        respuesta = "X";
      }
      if (this.preguntaLetraVisible === true) {
          if (this.promise !== null) {
            $timeout.cancel(this.promise);
            this.promise = null;
          }
          this.respuestasLetras.push([this.indiceGruposLetras, this.indiceLetras, respuesta]);
          this.ponerProximaLetra();
      }
    }.bind($scope);

    $scope.anularRespuestaLetra = function() {
      if (this.preguntaLetraVisible === true) {
        this.respuestasLetras.push([this.indiceGruposLetras, this.indiceLetras, 'X']);
        this.ponerProximaLetra();
      }
    }.bind($scope);

    $timeout($scope.ponerProximaSecuencia, $scope.t_prev);
  });

})();