(function(){

  var parenExperApp = angular.module('parenExperApp');

  parenExperApp.factory('$resultados', function() {
    return {
      inmediato: {
        respuestas: [],
      },
      inconsciente: {
        respuestas: [],
        respuestasLetras: [],
      },
      encuesta: {
      },
    };
  });

})();