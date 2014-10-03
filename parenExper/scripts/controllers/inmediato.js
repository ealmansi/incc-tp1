(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('inmediatoExplicacionCtlr', function($scope, $experimento) {
    $scope.t_expo = $experimento.inmediato.t_expo;
    $scope.t_resp = $experimento.inmediato.t_resp;

    $scope.avanzar = function () {
      this.avanzarDesde('inmediato-explicacion');
    }.bind($scope);
  });

  //esto es para focusear el div de la pregunta que capta las teclas
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

  parenExperCtlrs.controller('inmediatoExperimentoCtlr', function($scope, $timeout, $experimento, $resultados) {
    
    //timer
    var start, end;
 

    $scope.t_prev = $experimento.inmediato.t_prev;
    $scope.t_expo_6 = $experimento.inmediato.t_expo_6;
    $scope.t_expo_12 = $experimento.inmediato.t_expo_12;
    $scope.t_expo_18 = $experimento.inmediato.t_expo_18;


    $scope.t_resp = $experimento.inmediato.t_resp;
    $scope.secuencias = $experimento.inmediato.secuencias;
    $scope.respuestas = $resultados.inmediato.respuestas;

    $scope.avanzar = function () {
      this.avanzarDesde('inmediato-experimento');
    }.bind($scope);

    $scope.preparateVisible = true;
    $scope.secuenciaVisible = false;
    $scope.preguntaVisible = false;
    $scope.promise = null;
    $scope.indiceSecuencias = -1;

    $scope.ponerProximaSecuencia = function() {
      $('#no').css("background-color", "white");
      $('#si').css("background-color", "white");
      if (this.indiceSecuencias + 1 < this.secuencias.length) {
        this.indiceSecuencias = this.indiceSecuencias + 1;
        this.preguntaVisible = false;
        this.promise = $timeout(this.comenzarExposicion,1000);
      }
      else {
        this.avanzar();
      }
    }.bind($scope);

    // $scope.clickOnUpload = function () {
    //   $timeout(function() {
    //   angular.element('#hola').triggerHandler('click');
    //   }, 100);
    // };

    $scope.comenzarExposicion = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = true;
      this.preguntaVisible = false;
      var t_expo = 0;
      var largo = $experimento.inmediato.secuencias[this.indiceSecuencias].largo; 
      if(largo == 6){
        t_expo = this.t_expo_6;
      }
      else if(largo == 12){
        t_expo = this.t_expo_12;
      }
      else{
        t_expo = this.t_expo_18;
      }
      this.promise = $timeout(this.ocultarSecu, t_expo);
    }.bind($scope);

    $scope.ocultarSecu = function() {
      this.secuenciaVisible = false;
      this.promise = $timeout(this.terminarExposicion, 800);

    }.bind($scope);

    $scope.terminarExposicion = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = true;
      start = (new Date()).getTime();
 
// Run a test
 
      this.promise = $timeout(this.anularRespuesta, this.t_resp);
    }.bind($scope);
    
    $scope.registrarRespuesta = function(keyCode) {
      end = (new Date()).getTime();
 
      if(keyCode===78){ //codigo del No
        respuesta = "No";
        $('#no').css("background-color", "orange");
      }
      else if (keyCode === 83) //codigo del Si
      {
        respuesta = "Si";
        $('#si').css("background-color", "lightgreen");
      }
      else {
        respuesta = "X";
      }
      if (this.preguntaVisible === true) {
          if (this.promise !== null) {
            $timeout.cancel(this.promise);
            this.promise = null;
          }

          switch(this.secuencias[this.indiceSecuencias].largo)
          {
            case 6:
              indiceRta = 0;
              break;
            case 12:
              indiceRta = 1;
              break;
            case 18:
              indiceRta = 2;
              break;
          }
          // alert(indiceRta);
          if(respuesta === this.secuencias[this.indiceSecuencias].correcta){
            $resultados.inmediato.rtas_correctas[indiceRta]++;
          }

          this.respuestas.push([this.indiceSecuencias, respuesta, end-start]);
          this.promise = $timeout(this.ponerProximaSecuencia, 300);
      }
    }.bind($scope);

    $scope.anularRespuesta = function() {
      if (this.preguntaVisible === true) {
        $scope.registrarRespuesta('99'); //cualquier valor, pone una X
        // this.respuestas.push([this.indiceSecuencias, 'X']);
        // this.ponerProximaSecuencia();
      }
    }.bind($scope);

    $timeout($scope.ponerProximaSecuencia, $scope.t_prev);
  });

})();