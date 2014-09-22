(function(){
  
  var parenExperApp = angular.module('parenExperApp', ['ngRoute', 'parenExperCtlrs']);

  parenExperApp.config(function($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl : 'views/intro.html',
        controller  : 'introCtlr as ctlr'
      })
      .when('/primera-parte-intro', {
        templateUrl : 'views/primera-parte-intro.html',
        controller  : 'primeraParteIntroCtlr as ctlr'
      })
      .when('/primera-parte-exper', {
        templateUrl : 'views/primera-parte-exper.html',
        controller  : 'primeraParteExperCtlr as ctlr'
      })
      .when('/segunda-parte-intro', {
        templateUrl : 'views/segunda-parte-intro.html',
        controller  : 'segundaParteIntroCtlr as ctlr'
      })
      .when('/segunda-parte-exper', {
        templateUrl : 'views/segunda-parte-exper.html',
        controller  : 'segundaParteExperCtlr as ctlr'
      })
      .when('/contact', {
        templateUrl : 'views/contact.html',
        controller  : 'contactCtlr as ctlr'
      });
  });

  parenExperApp.run(function($rootScope, $location) {
    $rootScope.go = function(path) {
      $location.path(path);
    };
  });

  parenExperApp.directive('ngEnter', function () {
    return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.ngEnter);
                });

                event.preventDefault();
            }
        });
      };
  });

})();