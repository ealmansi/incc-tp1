(function(){

  var parenExperApp = angular.module('parenExperApp');

  parenExperApp.factory('$resultados', function() {
    return {
      respuestasInmediato: [],
      respuestasConsciente: [],
      respuestasInconsciente: [],
    };
  });

})();