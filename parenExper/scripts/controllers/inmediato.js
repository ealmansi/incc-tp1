(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('inmediatoExplicacionCtlr', function($scope, $experimento) {
    $scope.t_expo = $experimento.inmediato.t_expo;
    $scope.t_resp = $experimento.inmediato.t_resp;

    $scope.avanzar = function () {
      this.avanzarDesde('inmediato-explicacion');
    }.bind($scope);
  });

  parenExperCtlrs.controller('inmediatoExperimentoCtlr', function($scope, $timeout, $experimento, $resultados) {
    $scope.t_prev = $experimento.inmediato.t_prev;
    $scope.t_expo = $experimento.inmediato.t_expo;
    $scope.t_resp = $experimento.inmediato.t_resp;
    $scope.secuencias = $experimento.inmediato.secuencias;
    $scope.respuestas = $resultados.respuestasInmediato;

    $scope.avanzar = function () {
      this.avanzarDesde('inmediato-experimento');
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
    $scope.promise = null;
    $scope.indiceSecuencias = -1;

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
      this.promise = $timeout(this.terminarExposicion, this.t_expo);
    }.bind($scope);

    $scope.terminarExposicion = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = true;
      this.promise = $timeout(this.anularRespuesta, this.t_resp);
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