(function(){

  var parenExperApp = angular.module('parenExperApp');

  parenExperApp.factory('$experimento', function() {
    return {
      inmediato: {
        t_prev: 2000,           // tiempo de espera previo a empezar
        t_expo: 2000,           // tiempo de exposicion al estimulo
        t_resp: 2000,           // tiempo para responder
        t_buff: 50,             // tiempo buffer despues de apretar una tecla
        secuencias: [
          '{()}[[]][[][]]',
          '([]){[[]]}[]{}',
          '{(())}{{}}[][]',
          '[(){}][]({}())',
        ],
      },

      consciente: {
        t_prev: 1000,           // tiempo de espera previo a empezar
        t_expo: 4000,           // tiempo de exposicion al estimulo
        t_resp: 4000,           // tiempo para responder
        t_buff: 50,             // tiempo buffer despues de apretar una tecla
        secuencias: [
          '{()}[[]][[][]]',
          '([]){[[]]}[]{}',
          '{(())}{{}}[][]',
          '[(){}][]({}())',
        ],
      },

      inconsciente: {
        t_prev: 1000,           // tiempo de espera previo a empezar
        t_expo: 1000,           // tiempo de exposicion al estimulo
        t_resp: 1000,           // tiempo para responder
        secuencias: [
          '{()}[[]][[][]]',
          '([]){[[]]}[]{}',
          '{(())}{{}}[][]',
          '[(){}][]({}())',
        ],
        n_letras: 2,              // n de tarea distractoria
        t_prev_letras: 500,       // tiempo de espera antes de la tarea secundaria
        t_expo_letras: 500,       // cada letra se muestra 500ms
        t_resp_letras: 500,       // la respuesta se da en 2000ms
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