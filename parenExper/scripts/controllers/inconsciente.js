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

  parenExperCtlrs.controller('inconscienteExperimentoCtlr', function($scope, $timeout, $experimento) {
    $scope.t_prev = $experimento.inconsciente.t_prev;
    $scope.t_expo = $experimento.inconsciente.t_expo;
    $scope.t_resp = $experimento.inconsciente.t_resp;
    $scope.secuencias = $experimento.inconsciente.secuencias;
    $scope.respuestas = $resultados.inconsciente.respuestas;
    $scope.t_prev_letras = $experimento.inconsciente.t_prev_letras;
    $scope.t_expo_letras = $experimento.inconsciente.t_expo_letras;
    $scope.t_resp_letras = $experimento.inconsciente.t_resp_letras;
    $scope.letras = $experimento.inconsciente.letras;
    $scope.respuestasLetras = $resultados.inconsciente.respuestasLetras;

    $scope.avanzar = function () {
      this.avanzarDesde('inconsciente-experimento');
    }.bind($scope);

    $scope.$on('tecla-presionada', function(event, args) {
      if ('keyCode' in args) {
        if (args.keyCode == 115) {
          this.registrarRespuesta('S');
        }
        else if (args.keyCode == 110) {
          this.registrarRespuesta('N');
        }
      }
    }.bind($scope));

    $scope.preparateVisible = true;
    $scope.secuenciaVisible = false;
    $scope.preguntaVisible = false;
    $scope.letraVisible = false;
    $scope.promise = null;
    $scope.indiceSecuencias = -1;
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
      this.promise = $timeout(this.terminarExposicion, this.t_expo);
    }.bind($scope);

    $scope.terminarExposicion = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.letraVisible = false;
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
        this.preguntaVisible = true;
        this.letraVisible = false;
        this.promise = $timeout(this.anularRespuesta, this.t_resp);
        this.indiceLetras = -1;
      }
    }.bind($scope);

    $scope.comenzarExposicionLetra = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.letraVisible = true;
      this.promise = $timeout(this.terminarExposicionLetra, this.t_expo_letras);
    }.bind($scope);

    $scope.terminarExposicionLetra = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.letraVisible = false;
      this.promise = $timeout(this.ponerProximaLetra, this.t_resp_letras);
    }.bind($scope);

    $scope.registrarRespuesta = function(respuesta) {
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

    $timeout($scope.ponerProximaSecuencia, $scope.t_prev);
  });

})();