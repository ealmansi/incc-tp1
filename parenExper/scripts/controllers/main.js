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
      };
      $location.path(siguiente[ubicacionActual]);
    };
  });

})();