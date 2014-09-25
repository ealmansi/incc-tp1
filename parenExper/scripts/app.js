(function(){
  
  var parenExperApp = angular.module('parenExperApp', ['ngRoute', 'parenExperCtlrs', 'firebase']);
  var parenExperCtlrs = angular.module('parenExperCtlrs', []);

  parenExperApp.config(function($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl : 'views/introduccion.html',
        controller  : 'introduccionCtlr'
      })
      .when('/inm1', {
        templateUrl : 'views/inmediato-explicacion.html',
        controller  : 'inmediatoExplicacionCtlr'
      })
      .when('/inm2', {
        templateUrl : 'views/inmediato-experimento.html',
        controller  : 'inmediatoExperimentoCtlr'
      })
      .when('/con1', {
        templateUrl : 'views/consciente-explicacion.html',
        controller  : 'conscienteExplicacionCtlr'
      })
      .when('/con2', {
        templateUrl : 'views/consciente-experimento.html',
        controller  : 'conscienteExperimentoCtlr'
      })
      .when('/inc1', {
        templateUrl : 'views/inconsciente-explicacion.html',
        controller  : 'inconscienteExplicacionCtlr'
      })
      .when('/inc2', {
        templateUrl : 'views/inconsciente-experimento.html',
        controller  : 'inconscienteExperimentoCtlr'
      })
      .when('/enc', {
        templateUrl : 'views/encuesta.html',
        controller  : 'encuestaCtlr'
      })
      .when('/fin', {
        templateUrl : 'views/fin.html',
      })
  });

  parenExperApp.run(function ($templateCache, $http) {
    $http.get('views/introduccion.html', {cache: $templateCache});
    $http.get('views/inmediato-explicacion.html', {cache: $templateCache});
    $http.get('views/inmediato-experimento.html', {cache: $templateCache});
    $http.get('views/consciente-explicacion.html', {cache: $templateCache});
    $http.get('views/consciente-experimento.html', {cache: $templateCache});
    $http.get('views/inconsciente-explicacion.html', {cache: $templateCache});
    $http.get('views/inconsciente-experimento.html', {cache: $templateCache});
    $http.get('views/encuesta.html', {cache: $templateCache});
    $http.get('views/fin.html', {cache: $templateCache});
  });

})();