(function(){

  var parenExperCtlrs = angular.module('parenExperCtlrs', []);

  parenExperCtlrs.controller('introCtlr', function($scope) {
  });

  parenExperCtlrs.controller('primeraParteIntroCtlr', function($scope) {
    $scope.t_expo = 5;       // duracion del estimulo (segs)
    $scope.t_resp = 5;       // duracion del estimulo (segs)
  });

  parenExperCtlrs.controller('primeraParteExperCtlr', function($scope, $timeout) {
    $scope.t_prev = 2000;       // pausa antes de arrancar
    $scope.t_expo = 5000;       // duracion del estimulo
    $scope.t_resp = 5000;       // duracion del estimulo
    $scope.preparateVisible = true;
    $scope.secuenciaVisible = false;
    $scope.preguntaVisible = false;
    $scope.indice = 0;
    $scope.secuencias = [
      '{()}[[]][[][]]',
      '([]){[[]]}[]{}',
      '{(())}{{}}[][]',
      '[(){}][]({}())',
    ];

    $scope.mostrarSecuencia = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = true;
      this.preguntaVisible = false;
      $timeout(this.obtenerRespuesta, this.t_expo);
    }.bind($scope);

    $scope.obtenerRespuesta = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = true;
      if (this.indice + 1 < this.secuencias.length) {
        this.indice = this.indice + 1;
        $timeout(this.mostrarSecuencia, this.t_resp);
      }
      else {
        $timeout(function() {
          this.go('/segunda-parte-intro');
        }.bind(this), this.t_resp);
      }
    }.bind($scope);

    if ($scope.indice + 1 < $scope.secuencias.length) {
      $timeout($scope.mostrarSecuencia, $scope.t_prev);
    }
  });

// Segunda Parte
  parenExperCtlrs.controller('segundaParteIntroCtlr', function($scope) {
    $scope.t_expo = 15;       // duracion del estimulo (segs)
    $scope.t_resp = 5;       // duracion del estimulo (segs)
  });

  parenExperCtlrs.controller('segundaParteExperCtlr', function($scope, $timeout) {
    $scope.t_prev = 2000;       // pausa antes de arrancar
    $scope.t_expo = 15000;       // duracion del estimulo
    $scope.t_resp = 5000;       // duracion del estimulo
    $scope.preparateVisible = true;
    $scope.secuenciaVisible = false;
    $scope.preguntaVisible = false;
    $scope.indice = 0;
    $scope.secuencias = [
      '{()}[[]][[][]]',
      '([]){[[]]}[]{}',
      '{(())}{{}}[][]',
      '[(){}][]({}())',
    ];

    $scope.mostrarSecuencia = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = true;
      this.preguntaVisible = false;
      $timeout(this.obtenerRespuesta, this.t_expo);
    }.bind($scope);

    $scope.obtenerRespuesta = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = true;
      if (this.indice + 1 < this.secuencias.length) {
        this.indice = this.indice + 1;
        $timeout(this.mostrarSecuencia, this.t_resp);
      }
      else {
        $timeout(function() {
          this.go('/segunda-parte-intro');
        }.bind(this), this.t_resp);
      }
    }.bind($scope);

    if ($scope.indice + 1 < $scope.secuencias.length) {
      $timeout($scope.mostrarSecuencia, $scope.t_prev);
    }
  });


  // Tercera parte
  parenExperCtlrs.controller('terceraParteIntroCtlr', function($scope) {
    $scope.t_expo = 5;       // duracion del estimulo (segs)
    $scope.t_resp = 5;       // duracion del estimulo (segs)
    $scope.n_tarea = 2;      // n de tarea distractoria
  });

  parenExperCtlrs.controller('terceraParteExperCtlr', function($scope, $timeout) {
    $scope.t_prev = 2000;       // pausa antes de arrancar
    $scope.t_expo = 5000;       // duracion del estimulo
    $scope.t_resp = 5000;       // duracion del estimulo
    $scope.preparateVisible = true;
    $scope.secuenciaVisible = false;
    $scope.preguntaVisible = false;
    $scope.indice = 0;
    $scope.secuencias = [
      '{()}[[]][[][]]',
      '([]){[[]]}[]{}',
      '{(())}{{}}[][]',
      '[(){}][]({}())',
    ];

    //tarea
    $scope.t_expo_tarea = 500;  //cada letra se muestra 500ms
    $scope.t_resp_tarea = 2000; // la respuesta se da en 2000ms
    $scope.letrasVisible = false;
    $scope.indiceLetras = 0;
    $scope.letras = [
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
    ];

    $scope.mostrarSecuencia = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = true;
      this.preguntaVisible = false;
      this.tareaVisible = false;
      $timeout(this.mostrarTarea, this.t_expo);
    }.bind($scope);

    $scope.mostrarTarea = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.tareaVisible = true;
      $timeout(this.obtenerRespuestaTarea, this.t_expo_tarea);
    }.bind($scope);

    $scope.obtenerRespuesta = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = true;
      this.tareaVisible = false;
      this.indiceLetras = 0;
      if (this.indice + 1 < this.secuencias.length) {
        this.indice = this.indice + 1;
        $timeout(this.mostrarSecuencia, this.t_resp);
      }
      else {
        $timeout(function() {
          this.go('/tercera-parte-intro');
        }.bind(this), this.t_resp);
      }
    }.bind($scope);

    //rta tarea
    $scope.obtenerRespuestaTarea = function() {
      this.preparateVisible = false;
      this.secuenciaVisible = false;
      this.preguntaVisible = false;
      this.tareaVisible = false;
      if (this.indiceLetras + 1 < this.letras.length) {
        this.indiceLetras = this.indiceLetras + 1;
        $timeout(this.mostrarTarea, this.t_resp_tarea);
      }
      else {
        $timeout($scope.obtenerRespuesta, $scope.t_prev);
      }
    }.bind($scope);

    if ($scope.indice + 1 < $scope.secuencias.length) {
      $timeout($scope.mostrarSecuencia, $scope.t_prev);
    }
  });

 


})();