(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('conscienteExplicacionCtlr', function($scope, $experimento) {
    $scope.t_expo = $experimento.consciente.t_expo;
    $scope.t_resp = $experimento.consciente.t_resp;

    $scope.avanzar = function () {
      this.avanzarDesde('consciente-explicacion');
    }.bind($scope);
  });

  parenExperCtlrs.controller('conscienteExperimentoCtlr', function($scope, $timeout, $experimento) {
    $scope.t_prev = $experimento.consciente.t_prev;
    $scope.t_expo = $experimento.consciente.t_expo;
    $scope.t_resp = $experimento.consciente.t_resp;
    $scope.secuencias = $experimento.consciente.secuencias;
    
    $scope.preparateVisible = true;
    $scope.secuenciaVisible = false;
    $scope.preguntaVisible = false;
    $scope.indiceSecuencias = 0;

    $scope.mostrarSecuencia = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = true;
      this.preguntaVisible = false;
      $timeout(this.obtenerRespuesta, this.t_expo);
    }.bind($scope);

    $scope.obtenerRespuesta = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = true;
      if (this.indiceSecuencias + 1 < this.secuencias.length) {
        this.indiceSecuencias = this.indiceSecuencias + 1;
        $timeout(this.mostrarSecuencia, this.t_resp);
      }
      else {
        $timeout(function() {
          this.avanzarDesde('consciente-experimento');
        }.bind(this), this.t_resp);
      }
    }.bind($scope);

    if ($scope.indiceSecuencias + 1 < $scope.secuencias.length) {
      $timeout($scope.mostrarSecuencia, $scope.t_prev);
    }
  });

})();