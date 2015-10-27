var app = angular.module('modulo', []);
	app.controller('controle', ['$scope', function($scope){

		$scope.sobreNome = function(){
			$scope.texto = 'sena ferreira';
		};
	}]);
