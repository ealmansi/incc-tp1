(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('encuestaCtlr', function($scope, $resultados, $firebase, $http) {
    $scope.encuesta = $resultados.encuesta;
    $scope.rtas_correctas = $resultados.inmediato.rtas_correctas[0];

    $scope.enviarFormulario = function() {
      var ref = new Firebase('https://incc-tp1.firebaseio.com');
      ref.child('resultados').push($resultados);
      $scope.avanzarDesde('encuesta');
    };
  });

})();