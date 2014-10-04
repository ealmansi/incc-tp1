(function(){

  var parenExperApp = angular.module('parenExperApp');

  parenExperApp.factory('$experimento', function() {
    return {
      inmediato: {
        t_prev: 2000,           // tiempo de espera previo a empezar
        t_expo_6: 250,
        t_expo_12: 520,
        t_expo_18: 1000,           // tiempo de expoSicion al estimulo
        t_resp: 3000,           // tiempo para responder
        secuencias: [
          {secu:'([{}])[][{}]', largo: 12, correcta: 'si', depth:3},
          {secu:'()[[]]([])()', largo: 12, correcta: 'si', depth:2},
          {secu:'[]{}}]', largo: 6, correcta: 'no', depth:1},
          {secu:'[][[]]', largo: 6, correcta: 'si', depth:2},
          {secu:'{}())}{}()[]', largo: 12, correcta: 'no', depth:1},
          {secu:'[][][][]()[]{}(){}', largo: 18, correcta: 'si', depth:1},
          {secu:'()()(){}([])()[{[]', largo: 18, correcta: 'no', depth:2},
          {secu:'()[]()(){)()()[][]', largo: 18, correcta: 'no', depth:1},
          {secu:'[{}][{}]{}[]', largo: 12, correcta: 'si', depth:2},
          {secu:'{}{}{}[][{[]', largo: 12, correcta: 'no', depth:1},
          {secu:'(){}[]{}[](){}[]{}', largo: 18, correcta: 'si', depth:1},
          {secu:'{}[{}](){}{()}]]{}', largo: 18, correcta: 'no', depth:2},
          {secu:'{()})}', largo: 6, correcta: 'no', depth:3},
          {secu:'(){((}', largo: 6, correcta: 'no', depth:2},
          {secu:'[{[]}]({})[[]][][]', largo: 18, correcta: 'si', depth:3},
          {secu:'{[][]}{[]}[([])]{}', largo: 18, correcta: 'si', depth:3},
          {secu:'()[][]{}{}{}()[]{}', largo: 18, correcta: 'si', depth:1},
          {secu:'{(())}', largo: 6, correcta: 'si', depth:3},
          {secu:'()[][]{}[]]}', largo: 12, correcta: 'no', depth:1},
          {secu:'[]()[][)[][][][]{}', largo: 18, correcta: 'no', depth:1},
          {secu:'()[]{}', largo: 6, correcta: 'si', depth:1},
          {secu:'(){}}}', largo: 6, correcta: 'no', depth:2},
          {secu:'{(())}{}()()', largo: 12, correcta: 'si', depth:3},
          {secu:'[]{}()()[]{}', largo: 12, correcta: 'si', depth:1},
          {secu:'(){{()]}()()', largo: 12, correcta: 'no', depth:3},
          {secu:'{{}}{}', largo: 6, correcta: 'si', depth:2},
          {secu:'{[]}{{[]}}[{)]({})', largo: 18, correcta: 'no', depth:3},
          {secu:'{([]()', largo: 6, correcta: 'no', depth:1},
          {secu:'()()(){}([])()[][]', largo: 18, correcta: 'si', depth:2},
          {secu:'{}{{}}', largo: 6, correcta: 'si', depth:2},
          {secu:'()[{()}]{}[{}{}][]', largo: 18, correcta: 'si', depth:3},
          {secu:'[{(]}]({})[[]][][]', largo: 18, correcta: 'no', depth:3},
          {secu:'()[][()][]{}', largo: 12, correcta: 'si', depth:2},
          {secu:'{}[]()', largo: 6, correcta: 'si', depth:1},
          {secu:'([])[]{}[]()', largo: 12, correcta: 'si', depth:2},
          {secu:'(){[()]}()()', largo: 12, correcta: 'si', depth:3},
          {secu:'()()[])}(){[]}[]{}', largo: 18, correcta: 'no', depth:2},
          {secu:'{[]}{[[]]}()', largo: 12, correcta: 'si', depth:3},
          {secu:'{}(){}{}()[]', largo: 12, correcta: 'si', depth:1},
          {secu:'{[]}{{[]}}[{}]({})', largo: 18, correcta: 'si', depth:3},
          {secu:'{[]}]}', largo: 6, correcta: 'no', depth:3},
          {secu:'{(())}{{}()}([]){}', largo: 18, correcta: 'si', depth:3},
          {secu:'{}[][]', largo: 6, correcta: 'si', depth:1},
          {secu:'{}[]{]', largo: 6, correcta: 'no', depth:1},
          {secu:'[([])]', largo: 6, correcta: 'si', depth:3},
          {secu:'[](){}()()()', largo: 12, correcta: 'si', depth:1},
          {secu:'[][)]]', largo: 6, correcta: 'no', depth:2},
          {secu:'()[{()}]{}[{({}][]', largo: 18, correcta: 'no', depth:3},
          {secu:'()[][()][({}', largo: 12, correcta: 'no', depth:2},
          {secu:'{(]])}(())()', largo: 12, correcta: 'no', depth:3},
          {secu:'[][][][]()[]}}(){}', largo: 18, correcta: 'no', depth:1},
          {secu:'()[]()()()()()[][]', largo: 18, correcta: 'si', depth:1},
          {secu:'()[{}](())()([])()', largo: 18, correcta: 'si', depth:2},
          {secu:'{}[{}](){}{()}[]{}', largo: 18, correcta: 'si', depth:2},
          {secu:'{[{}]}', largo: 6, correcta: 'si', depth:3},
          {secu:'()[][]{}[]{}', largo: 12, correcta: 'si', depth:1},
          {secu:'{[][]}{[])[([])]{}', largo: 18, correcta: 'no', depth:3},
          {secu:'(){()}', largo: 6, correcta: 'si', depth:2},
          {secu:'[]{]()', largo: 6, correcta: 'no', depth:1},
          {secu:'(){}[]{}[]()(}[]{}', largo: 18, correcta: 'no', depth:1},
          {secu:'{([])}(())()', largo: 12, correcta: 'si', depth:3},
          {secu:'{}{()}({})[()]{()}', largo: 18, correcta: 'si', depth:2},
          {secu:'[]{[)}(){}[]', largo: 12, correcta: 'no', depth:2},
          {secu:'{[{}{[[]]}()', largo: 12, correcta: 'no', depth:3},
          {secu:'{{}}}}', largo: 6, correcta: 'no', depth:2},
          {secu:'({()})', largo: 6, correcta: 'si', depth:3},
          {secu:'()[](]{}{}{}()[]{}', largo: 18, correcta: 'no', depth:1},
          {secu:'{({})}', largo: 6, correcta: 'si', depth:3},
          {secu:'{(())({}()()', largo: 12, correcta: 'no', depth:3},
          {secu:'{}{{(}', largo: 6, correcta: 'no', depth:2},
          {secu:'{(()[}{{}()}([]){}', largo: 18, correcta: 'no', depth:3},
          {secu:'[]()[]()[][][][]{}', largo: 18, correcta: 'si', depth:1},
          {secu:'[](){{()()()', largo: 12, correcta: 'no', depth:1},
          {secu:'[]{}(}()[]{}', largo: 12, correcta: 'no', depth:1},
          {secu:'()[[]]([))()', largo: 12, correcta: 'no', depth:2},
          {secu:'[][]()', largo: 6, correcta: 'si', depth:1},
          {secu:'([{}))[][{}]', largo: 12, correcta: 'no', depth:3},
          {secu:'{}{}{}[][][]', largo: 12, correcta: 'si', depth:1},
          {secu:'()[{}](())(}([])()', largo: 18, correcta: 'no', depth:2},
          {secu:'{(()[}', largo: 6, correcta: 'no', depth:3},
          {secu:'()[{{}', largo: 6, correcta: 'no', depth:1},
          {secu:'[([]]]', largo: 6, correcta: 'no', depth:3},
          {secu:'[{}][{}][}[]', largo: 12, correcta: 'no', depth:2},
          {secu:'{}{()}({})[(){{()}', largo: 18, correcta: 'no', depth:2},
          {secu:'()()[]{}(){[]}[]{}', largo: 18, correcta: 'si', depth:2},
          {secu:'[]{}[]', largo: 6, correcta: 'si', depth:1},
          {secu:'([])[]{)[]()', largo: 12, correcta: 'no', depth:2},
          {secu:'[]{()}(){}[]', largo: 12, correcta: 'si', depth:2},
          {secu:'(){{}}', largo: 6, correcta: 'si', depth:2},
          {secu:'(]()})', largo: 6, correcta: 'no', depth:3},          
        ],
      },

      inconsciente: {
        t_prev: 2000,           // tiempo de espera previo a empezar
        t_expo: 1000,           // tiempo de expoSicion al estimulo
        t_resp: 5000,           // tiempo para responder
        secuencias: [
          {secu:'()[][()]({})({})[]', largo: 18, correcta: 'si', depth:2},
          {secu:'[][[(}]]()[[]][][]', largo: 18, correcta: 'no', depth:3},
          {secu:'{{}}[[]]{}{}]}{}{}', largo: 18, correcta: 'no', depth:3},
          {secu:'((()()()[][]{}(){}', largo: 18, correcta: 'no', depth:1},
          {secu:'{]{{}}[]([])()()[]', largo: 18, correcta: 'no', depth:2},
          {secu:'({[]})[[]{}]{()}()', largo: 18, correcta: 'si', depth:3},
          {secu:'{}(]{}[](){}[]{}{}', largo: 18, correcta: 'no', depth:1},
          {secu:'()[{}]()[](())(())', largo: 18, correcta: 'si', depth:2},
          {secu:'{}(){}[](){}[]{}{}', largo: 18, correcta: 'si', depth:1},
          {secu:'[][[{}]]()[[]][][]', largo: 18, correcta: 'si', depth:3},
          {secu:'()[][()]({})({})]]', largo: 18, correcta: 'no', depth:2},
          {secu:'{}()[]()[]{}{}[]()', largo: 18, correcta: 'si', depth:1},
          {secu:'[{}(}]({{}}){}{[]}', largo: 18, correcta: 'no', depth:3},
          {secu:'()[{}}()[](())(())', largo: 18, correcta: 'no', depth:2},
          {secu:'(())[]{({})}{()}{}', largo: 18, correcta: 'si', depth:3},
          {secu:'[{}{}]({{}}){}{[]}', largo: 18, correcta: 'si', depth:3},
          {secu:'[()}(())[]{}()(){}', largo: 18, correcta: 'no', depth:2},
          {secu:'[][]{}(]()[][][]()', largo: 18, correcta: 'no', depth:1},
          {secu:'[()](())[]{}()(){}', largo: 18, correcta: 'si', depth:2},
          {secu:'[]{}{}{}{}{}(){}()', largo: 18, correcta: 'si', depth:1},
          {secu:'{}()[](){]{}{}[]()', largo: 18, correcta: 'no', depth:1},
          {secu:'[]{}{}{[{}{}(){}()', largo: 18, correcta: 'no', depth:1},
          {secu:'[][]{}[]()[][][]()', largo: 18, correcta: 'si', depth:1},
          {secu:'{{}}(())[()]{()}[]', largo: 18, correcta: 'si', depth:2},
          {secu:'{}{{}}[]([])()()[]', largo: 18, correcta: 'si', depth:2},
          {secu:'(())[]{({})){()}{}', largo: 18, correcta: 'no', depth:3},
          {secu:'{{}}[[]]{[{}]}{}{}', largo: 18, correcta: 'si', depth:3},
          {secu:'()()()()[][]{}(){}', largo: 18, correcta: 'si', depth:1},
          {secu:'{{}}(()][()]{()}[]', largo: 18, correcta: 'no', depth:2},
          {secu:'({[]})[[]{}){()}()', largo: 18, correcta: 'no', depth:3},
        ],
        n_letras: 1,               // n de tarea distractoria
        t_prev_letras: 2000,       // tiempo de espera antes de la tarea secundaria
        t_expo_letras: 300,       // cada letra se muestra 500ms
        t_resp_letras: 1000,       // la respuesta se da en 2000ms
        t_buff_letras: 2000,       // intervalo despues de responder la ultima letra
        gruposLetras: [
          ['T','Z','Z','V','V','R','W','R','T','R','T','T','U','U','T'],// 4 2-back, 2 1-back, 2 3-back
          ['C','F','C','F','Z','F','F','F','O','G','O','P','W','P','P'],// 4 2-back, 2 1-back, 2 3-back 
          ['N','N','G','N','D','S','D','D','G','Y','D','D','G','W','Y'],// 4 2-back, 2 1-back, 2 3-back 
          ['O','C','Z','C','C','R','W','R','O','R','O','O','R','U','O'],// 4 2-back, 2 1-back, 2 3-back 
          ['F','F','G','F','D','S','D','D','G','G','G','D','G','W','Y'],// 4 2-back, 2 1-back, 2 3-back 
          ['C','E','C','Z','Z','H','E','E','O','G','O','W','W','A','A'],// 4 2-back, 2 1-back, 2 3-back 
        ]
      },
    };
  });

})();