(function(){

  var parenExperApp = angular.module('parenExperApp');

  parenExperApp.factory('$experimento', function() {
    return {
      inmediato: {
        t_prev: 1000,           // tiempo de espera previo a empezar
        t_expo: 1000,           // tiempo de exposicion al estimulo
        t_resp: 1000,           // tiempo para responder
        secuencias: [
          '{()}[[]][[][]]',
          '([]){[[]]}[]{}',
          '{(())}{{}}[][]',
          '[(){}][]({}())',
        ],
      },

      consciente: {
        t_prev: 1000,           // tiempo de espera previo a empezar
        t_expo: 1000,           // tiempo de exposicion al estimulo
        t_resp: 1000,           // tiempo para responder
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
        n_letras: 2,               // n de tarea distractoria
        t_prev_letras: 1000,       // tiempo de espera antes de la tarea secundaria
        t_expo_letras: 1000,       // cada letra se muestra 500ms
        t_resp_letras: 1000,       // la respuesta se da en 2000ms
        t_buff_letras: 500,       // intervalo despues de responder la ultima letra
        gruposLetras: [
          ['R','C','A','R','T',],//'M','R','R','E','C','A','R',],
          ['R','E','C','A','R',],//'R','C','A','R','T','M','R',],
          ['E','C','A','R','C',],//'A','R','R','T','M','R','R',],
        ],
      },
    };
  });

})();