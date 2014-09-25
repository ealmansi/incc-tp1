(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs');
  
  parenExperCtlrs.controller('mainCtlr', function($scope, $location) {

    $scope.avanzarDesde = function(ubicacionActual) {
      var siguiente = {
        'introduccion': '/inm1',
        'inmediato-explicacion': '/inm2',
        'inmediato-experimento': '/con1',
        'consciente-explicacion': '/con2',
        'consciente-experimento': '/inc1',
        'inconsciente-explicacion': '/inc2',
        'inconsciente-experimento': '/enc',
        'encuesta': '/fin',
      };
      $location.path(siguiente[ubicacionActual]);
    };

    $scope.broadcastTeclaPresionada = function($event) {
      $scope.$broadcast('tecla-presionada', {keyCode: $event.keyCode});
    };
  });

})();