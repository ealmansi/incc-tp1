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

})();