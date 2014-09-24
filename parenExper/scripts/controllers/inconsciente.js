(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('inconscienteExplicacionCtlr', function($scope, $experimento) {
    $scope.t_expo = $experimento.inconsciente.t_expo;
    $scope.t_resp = $experimento.inconsciente.t_resp;
    $scope.n_tarea = $experimento.inconsciente.n_tarea;
  });

  parenExperCtlrs.controller('inconscienteExperimentoCtlr', function($scope, $timeout, $experimento) {
    $scope.t_prev = $experimento.inconsciente.t_prev;
    $scope.secuencias = $experimento.inconsciente.secuencias;
    $scope.t_expo_tarea = $experimento.inconsciente.t_expo_tarea;
    $scope.t_resp_tarea = $experimento.inconsciente.t_resp_tarea;
    $scope.letras = $experimento.inconsciente.letras;
    
    $scope.preparateVisible = true;
    $scope.secuenciaVisible = false;
    $scope.preguntaVisible = false;
    $scope.letrasVisible = false;
    $scope.indice = 0;
    $scope.indiceLetras = 0;

    $scope.mostrarSecuencia = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = true;
      this.preguntaVisible = false;
      this.tareaVisible = false;
      $timeout(this.mostrarTarea, this.t_expo);
    }.bind($scope);

    $scope.mostrarTarea = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.tareaVisible = true;
      $timeout(this.obtenerRespuestaTarea, this.t_expo_tarea);
    }.bind($scope);

    $scope.obtenerRespuesta = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = true;
      this.tareaVisible = false;
      this.indiceLetras = 0;
      if (this.indice + 1 < this.secuencias.length) {
        this.indice = this.indice + 1;
        $timeout(this.mostrarSecuencia, this.t_resp);
      }
      else {
        $timeout(function() {
          this.avanzarDesde('inconsciente-experimento');
        }.bind(this), this.t_resp);
      }
    }.bind($scope);

    //rta tarea
    $scope.obtenerRespuestaTarea = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.tareaVisible = false;
      if (this.indiceLetras + 1 < this.letras.length) {
        this.indiceLetras = this.indiceLetras + 1;
        $timeout(this.mostrarTarea, this.t_resp_tarea);
      }
      else {
        $timeout($scope.obtenerRespuesta, $scope.t_prev);
      }
    }.bind($scope);

    if ($scope.indice + 1 < $scope.secuencias.length) {
      $timeout($scope.mostrarSecuencia, $scope.t_prev);
    }
  });

})();