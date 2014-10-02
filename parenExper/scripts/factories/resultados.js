(function(){

  var parenExperApp = angular.module('parenExperApp');

  parenExperApp.factory('$resultados', function() {
    return {
      inmediato: {
        respuestas: [],
        rtas_correctas: [0,0,0],
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