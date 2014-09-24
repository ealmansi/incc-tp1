(function(){

  var parenExperApp = angular.module('parenExperApp');

  parenExperApp.factory('$experimento', function() {
    return {
      inmediato: {
        t_prev: 500,           // tiempo de espera previo a empezar
        t_expo: 500,           // tiempo de exposicion al estimulo
        t_resp: 500,           // tiempo para responder
        secuencias: [
          '{()}[[]][[][]]',
          '([]){[[]]}[]{}',
          '{(())}{{}}[][]',
          '[(){}][]({}())',
        ],
      },
      consciente: {
        t_prev: 500,           // tiempo de espera previo a empezar
        t_expo: 500,           // tiempo de exposicion al estimulo
        t_resp: 500,           // tiempo para responder
        secuencias: [
          '{()}[[]][[][]]',
          '([]){[[]]}[]{}',
          '{(())}{{}}[][]',
          '[(){}][]({}())',
        ],
      },
      inconsciente: {
        t_prev: 2000,           // tiempo de espera previo a empezar
        t_expo: 5000,           // tiempo de exposicion al estimulo
        t_resp: 5000,           // tiempo para responder
        secuencias: [
          '{()}[[]][[][]]',
          '([]){[[]]}[]{}',
          '{(())}{{}}[][]',
          '[(){}][]({}())',
        ],
        n_tarea: 2,         // n de tarea distractoria
        t_expo_tarea: 500,  //cada letra se muestra 500ms
        t_resp_tarea: 2000, // la respuesta se da en 2000ms
        letras: [
          'R',
          'C',
          'A',
          'R',
          'T',
          'M',
          'R',
          'R',
          'E',
          'C',
          'A',
          'R',
        ],
      },
    };
  });

})();