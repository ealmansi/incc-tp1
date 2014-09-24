(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('inmediatoExplicacionCtlr', function($scope, $experimento) {
    $scope.t_expo = $experimento.inmediato.t_expo;
    $scope.t_resp = $experimento.inmediato.t_resp;
  });

  parenExperCtlrs.controller('inmediatoExperimentoCtlr', function($scope, $timeout, $experimento) {
    $scope.t_prev = $experimento.inmediato.t_prev;
    $scope.t_expo = $experimento.inmediato.t_expo;
    $scope.t_resp = $experimento.inmediato.t_resp;
    $scope.secuencias = $experimento.inmediato.secuencias;

    $scope.preparateVisible = true;
    $scope.secuenciaVisible = false;
    $scope.preguntaVisible = false;
    $scope.indice = 0;

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
      if (this.indice + 1 < this.secuencias.length) {
        this.indice = this.indice + 1;
        $timeout(this.mostrarSecuencia, this.t_resp);
      }
      else {
        $timeout(function() {
          this.avanzarDesde('inmediato-experimento');
        }.bind(this), this.t_resp);
      }
    }.bind($scope);

    if ($scope.indice + 1 < $scope.secuencias.length) {
      $timeout($scope.mostrarSecuencia, $scope.t_prev);
    }
  });

})();