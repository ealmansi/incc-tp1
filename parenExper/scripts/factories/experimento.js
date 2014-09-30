(function(){

  var parenExperApp = angular.module('parenExperApp');

  parenExperApp.factory('$experimento', function() {
    return {
      inmediato: {
        t_prev: 1000,           // tiempo de espera previo a empezar
        t_expo: 1000,           // tiempo de exposicion al estimulo
        t_resp: 3000,           // tiempo para responder
        secuencias: [
          '{[()]}',             // Máx 1 cebolla por nivel (3 niveles), correcto
          '([{}])',             // correcto
          '[({)]',              //1 incorrecto
          '{)[}',               //2 incorrectos
          '(){[()[]]{}}',       // Máx 2 cebollas por nivel (3 niveles), correcto
          '(({[]()}())[]',      //1 incorrecto
          '[]{{()[]}()}',       // correcto
          '(([[]{}](){}',       //2 incorrectos
          '{}({()[]()}[]())[]', // Máx 3 cebollas por nivel (3 niveles), correcto
          '{({()[]()}[]())[]',  //1 incorrecto
          '{({()[]{}}{}[]{',    //2 incorrectos
          '()[{()[]()}{()}][]'  //correcto
        ],
      },

      inconsciente: {
        t_prev: 1000,           // tiempo de espera previo a empezar
        t_expo: 1000,           // tiempo de exposicion al estimulo
        t_resp: 5000,           // tiempo para responder
        secuencias: [
          '{[()]}',             // Máx 1 cebolla por nivel (3 niveles), correcto
          '[({)]',              //1 incorrecto
          '{)[}',               //2 incorrectos
          '([{}])',             // correcto
          '(){[()[]]{}}',       // Máx 2 cebollas por nivel (3 niveles), correcto
          '(({[]()}())[]',      //1 incorrecto
          '(([[]{}](){}',       //2 incorrectos
          '[]{{()[]}()}',       // correcto
          '{}({()[]()}[]())[]', // Máx 3 cebollas por nivel (3 niveles), correcto
          '{({()[]()}[]())[]',  //1 incorrecto
          '()[{()[]()}{()}][]',  //correcto
          '{({()[]{}}{}[]{'   //2 incorrectos
        ],
        n_letras: 2,               // n de tarea distractoria
        t_prev_letras: 1000,       // tiempo de espera antes de la tarea secundaria
        t_expo_letras: 500,       // cada letra se muestra 500ms
        t_resp_letras: 2000,       // la respuesta se da en 2000ms
        t_buff_letras: 2000,       // intervalo despues de responder la ultima letra
        gruposLetras: [
          ['T','V','Z','V','V','R','W','R','T','R','T','T','R','U','T'],// 4 2-back, 2 1-back, 2 3-back
          ['C','F','C','F','Z','H','F','F','O','G','O','P','W','P','P'],// 4 2-back, 2 1-back, 2 3-back 
          ['N','N','G','N','D','S','D','D','G','Y','G','D','G','W','Y'],// 4 2-back, 2 1-back, 2 3-back 
          ['O','C','Z','C','C','R','W','R','O','R','O','O','R','U','O'],// 4 2-back, 2 1-back, 2 3-back 
          ['F','F','G','F','D','S','D','D','G','Y','G','D','G','W','Y'],// 4 2-back, 2 1-back, 2 3-back 
          ['C','E','C','E','Z','H','E','E','O','G','O','A','W','A','A'],// 4 2-back, 2 1-back, 2 3-back 
        ]
      },
    };
  });

})();