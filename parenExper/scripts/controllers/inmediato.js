(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('inmediatoExplicacionCtlr', function($scope, $experimento) {
    $scope.avanzar = function () {
      this.avanzarDesde('inmediato-explicacion');
    }.bind($scope);
  });

  parenExperCtlrs.controller('inmediatoExperimentoCtlr', function($scope, $timeout, $experimento, $resultados) {
    $scope.t_prev = $experimento.inmediato.t_prev;
    $scope.t_expo = $experimento.inmediato.t_expo;
    $scope.t_resp = $experimento.inmediato.t_resp;
    $scope.t_buff = $experimento.inmediato.t_buff;
    $scope.secuencias = $experimento.inmediato.secuencias;
    $scope.respuestas = $resultados.inmediato.respuestas;
    
    $scope.avanzar = function () {
      this.avanzarDesde('inmediato-experimento');
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
    }.bind($scope));

    $scope.preparateVisible = true;
    $scope.secuenciaVisible = false;
    $scope.preguntaVisible = false;
    $scope.promise = null;
    $scope.indiceSecuencias = -1;
    $scope.timerStart = null;
    $scope.timerEnd = null;

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
      this.timerStart = (new Date()).getTime();
      this.promise = $timeout(this.terminarExposicion, this.t_expo(this.secuencias[this.indiceSecuencias]));
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

    $timeout($scope.ponerProximaSecuencia, $scope.t_prev);
  });

})();