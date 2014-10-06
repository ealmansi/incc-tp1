(function(){

  var parenExperApp = angular.module('parenExperApp');

  parenExperApp.factory('$experimento', function() {
    return {
      inmediato: {
        t_prev: 2000,           // tiempo de espera previo a empezar
        t_expo: function(s){    // tiempo de exposicion al estimulo
          var length_tiempo = {
            6:    300,
            12:   520,
            18:   1000,
          };
          if (s.length in length_tiempo) {
            return length_tiempo[s.length];
          }
          return 1000;
        },
        t_resp: 5000,           // tiempo para responder
        t_buff: 50,             // tiempo buffer despues de responder
        secuencias: [
          '[[]][]()({}{[[]]()', //largo: 18, correcta: 'no', depth:2},
          '{}()[]([]){{}}([()', //largo: 18, correcta: 'no', depth:2},
          '(){}(){}{}(){}(][]', //largo: 18, correcta: 'no', depth:1},
          '{([})}[()]{}', //largo: 12, correcta: 'no', depth:3},
          '[[]][]()({})[[]]()', //largo: 18, correcta: 'si', depth:2},
          '[(()[]', //largo: 6, correcta: 'no', depth:3},
          '[[]]{}', //largo: 6, correcta: 'si', depth:2},
          '[]{}[]', //largo: 6, correcta: 'si', depth:1},
          '{][]()', //largo: 6, correcta: 'no', depth:1},
          '()[]{}{()}{}', //largo: 12, correcta: 'si', depth:2},
          '[)]]{}', //largo: 6, correcta: 'no', depth:2},
          '(([]{}{()}{}', //largo: 12, correcta: 'no', depth:2},
          '[[{}[]', //largo: 6, correcta: 'no', depth:1},
          '{({})}[()]{}', //largo: 12, correcta: 'si', depth:3},
          '{}[]()', //largo: 6, correcta: 'si', depth:1},
          '{({))}', //largo: 6, correcta: 'no', depth:3},
          '[()]()]]{[]}', //largo: 12, correcta: 'no', depth:2},
          '[]{}[][]{}{}{}{}{}', //largo: 18, correcta: 'si', depth:1},
          '[][]()[][][]', //largo: 12, correcta: 'si', depth:1},
          '[]{}[]{}[]{}', //largo: 12, correcta: 'si', depth:1},
          '{[]}{}', //largo: 6, correcta: 'si', depth:2},
          '[][][]{()}([])[[}]', //largo: 18, correcta: 'no', depth:2},
          '{[]}({})[{}]', //largo: 12, correcta: 'si', depth:2},
          '[[[]{]({}){}', //largo: 12, correcta: 'no', depth:3},
          '[][]()}][][]', //largo: 12, correcta: 'no', depth:1},
          '([[]{}', //largo: 6, correcta: 'no', depth:1},
          '()[][[}[]][(())]{}', //largo: 18, correcta: 'no', depth:3},
          '()[][{}[]][(())]{}', //largo: 18, correcta: 'si', depth:3},
          '{({})}', //largo: 6, correcta: 'si', depth:3},
          '{[]}]}', //largo: 6, correcta: 'no', depth:2},
          '[(()[]', //largo: 6, correcta: 'no', depth:3},
          '[]{}[{{}[]{}', //largo: 12, correcta: 'no', depth:1},
          '(())()', //largo: 6, correcta: 'si', depth:2},
          '[]{}{}({{}[]', //largo: 12, correcta: 'no', depth:1},
          '()[]{}', //largo: 6, correcta: 'si', depth:1},
          '[()]()[]{[]}', //largo: 12, correcta: 'si', depth:2},
          '[][()]({()}){[(){}', //largo: 18, correcta: 'no', depth:3},
          '([]){}[({])]', //largo: 12, correcta: 'no', depth:3},
          '{}()[{})}]{}[()]{}', //largo: 18, correcta: 'no', depth:3},
          '[][()]({()}){}(){}', //largo: 18, correcta: 'si', depth:3},
          '(){}(){}{}(){}[][]', //largo: 18, correcta: 'si', depth:1},
          '[]{}{}[][](([][]()', //largo: 18, correcta: 'no', depth:1},
          '[]{}{}(){}[]', //largo: 12, correcta: 'si', depth:1},
          '[][][]{()}([])[[]]', //largo: 18, correcta: 'si', depth:2},
          '[]{}{}[][]()[][]()', //largo: 18, correcta: 'si', depth:1},
          '{}()[{()}]{}[()]{}', //largo: 18, correcta: 'si', depth:3},
          '[(())]', //largo: 6, correcta: 'si', depth:3},
          '[]{}]][]{}{}{}{}{}', //largo: 18, correcta: 'no', depth:1},
          '{)]}({})[{}]', //largo: 12, correcta: 'no', depth:2},
          '[(())]', //largo: 6, correcta: 'si', depth:3},
          '{}()[]([]){{}}([])', //largo: 18, correcta: 'si', depth:2},
          '([]){}[([])]', //largo: 12, correcta: 'si', depth:3},
          '[[[]]]({}){}', //largo: 12, correcta: 'si', depth:3},
          '(({)()', //largo: 6, correcta: 'no', depth:2},
        ],
      },

      inconsciente: {
        t_prev: 2000,           // tiempo de espera previo a empezar
        t_expo: function(s){    // tiempo de exposicion al estimulo
          var length_tiempo = {
            6:    300,
            12:   520,
            18:   1000,
          };
          if (s.length in length_tiempo) {
            return length_tiempo[s.length];
          }
          return 1000;
        },
        t_resp: 5000,           // tiempo para responder
        t_buff: 150,             // tiempo buffer despues de responder
        secuencias: [
          '[]{{}}})[[]]{}[]()', //largo: 18, correcta: 'no', depth:2},
          '[]()()(}()()[](){}', //largo: 18, correcta: 'no', depth:1},
          '()[][](){}])[][]{}', //largo: 18, correcta: 'no', depth:1},
          '[][{}]{}({})({}){}', //largo: 18, correcta: 'si', depth:2},
          '()()[][]{({}{}{}{}', //largo: 18, correcta: 'no', depth:1},
          '([[]])([()]){{}}()', //largo: 18, correcta: 'si', depth:3},
          '()[][](){}()[][]{}', //largo: 18, correcta: 'si', depth:1},
          '()()[][]{}{}{}{}{}', //largo: 18, correcta: 'si', depth:1},
          '([[]])([])]){{}}()', //largo: 18, correcta: 'no', depth:3},
          '{}([()([])[](())[]', //largo: 18, correcta: 'no', depth:2},
          '[]()(){}()()[](){}', //largo: 18, correcta: 'si', depth:1},
          '{}{[()]}[()]({[)[]', //largo: 18, correcta: 'no', depth:3},
          '[][][][(())]{}{}()', //largo: 18, correcta: 'si', depth:3},
          '[][{}]{}({}(({}){}', //largo: 18, correcta: 'no', depth:2},
          '{}([])([])[](())[]', //largo: 18, correcta: 'si', depth:2},
          '[][][][(())]{}{{()', //largo: 18, correcta: 'no', depth:3},
          '{}{[()]}[()]({})[]', //largo: 18, correcta: 'si', depth:3},
          '[]{{}}()[[]]{}[]()', //largo: 18, correcta: 'si', depth:2},
        ],
        n_letras: 1,               // n de tarea distractoria
        t_prev_letras: 1000,       // tiempo de espera antes de la tarea secundaria
        t_expo_letras: 600,       // cada letra se muestra 500ms
        t_resp_letras: 15000,       // la respuesta se da en 2000ms
        t_buff_letras: 1000,       // intervalo despues de responder la ultima letra
        gruposLetras: [
          ['T','Z','Z','V','V'],//,'R','W','R','T','R','T','T','U','U','T'],// 4 2-back, 2 1-back, 2 3-back
          ['C','F','C','F','Z'],//,'F','F','F','O','G','O','P','W','P','P'],// 4 2-back, 2 1-back, 2 3-back 
          ['N','N','G','N','D'],//,'S','D','D','G','Y','D','D','G','W','Y'],// 4 2-back, 2 1-back, 2 3-back 
          ['O','C','Z','C','C'],//,'R','W','R','O','R','O','O','R','U','O'],// 4 2-back, 2 1-back, 2 3-back 
          ['F','F','G','F','D'],//,'S','D','D','G','G','G','D','G','W','Y'],// 4 2-back, 2 1-back, 2 3-back 
          ['C','E','C','Z','Z'],//,'H','E','E','O','G','O','W','W','A','A'],// 4 2-back, 2 1-back, 2 3-back 
        ]
      },
    };
  });

})();