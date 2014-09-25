(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');

  parenExperCtlrs.controller('encuestaCtlr', function($scope, $resultados, $firebase, $http) {
    $scope.encuesta = $resultados.encuesta;

    $scope.enviarFormulario = function() {
      var ref = new Firebase('https://incc-tp1.firebaseio.com');
      ref.child('resultados').push($resultados);
      $scope.avanzarDesde('encuesta');
    };
  });

})();