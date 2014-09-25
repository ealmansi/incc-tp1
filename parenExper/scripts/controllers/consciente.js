(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('conscienteExplicacionCtlr', function($scope, $experimento) {
    $scope.t_expo = $experimento.consciente.t_expo;
    $scope.t_resp = $experimento.consciente.t_resp;

    $scope.avanzar = function () {
      this.avanzarDesde('consciente-explicacion');
    }.bind($scope);
  });

  parenExperCtlrs.controller('conscienteExperimentoCtlr', function($scope, $timeout, $experimento, $resultados) {
    $scope.t_prev = $experimento.consciente.t_prev;
    $scope.t_expo = $experimento.consciente.t_expo;
    $scope.t_resp = $experimento.consciente.t_resp;
    $scope.secuencias = $experimento.consciente.secuencias;
    $scope.respuestas = $resultados.consciente.respuestas;

    $scope.avanzar = function () {
      this.avanzarDesde('consciente-experimento');
    }.bind($scope);

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