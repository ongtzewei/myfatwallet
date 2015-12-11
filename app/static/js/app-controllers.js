(function() {
	"use strict";
	var app = angular.module("walletApp");
	app.factory("Inventory", ["$rootScope", "$resource", function($rootScope, $resource) {
		var actions = {
			get: {method:"GET",withCredentials:true},
			put: {method:"PUT",withCredentials:true},
			post: {method:"POST",withCredentials:true},
			delete: {method:"DELETE",withCredentials:true},
		};
		return $resource($rootScope.wallet.URL.AppInventory, null, actions);
	}]);
	app.controller("ListingCtrl", function($scope, $stateParams, Inventory) {
		$scope.name = "App Listing Controller";
		$scope.initListing = function() {
			$scope.inventory = [];
			Inventory.get(function(response) {
				$scope.inventory = response.results;
			});
		};
	});
	app.controller("DashboardCtrl", function($scope) {
		$scope.name = "App Dashboard Controller";
		$scope.initDashboard = function() {
			$scope.total_takings = "$710.10"
			$scope.revenue_data = [
				{label: "Mixed Rice", value: 78, color: "#2ca02c"},
				{label: "Hokkien Mee", value: 68, color: "#1f77b4"},
				{label: "Bee Hoon", value: 57, color: "#ff7f0e"},
				{label: "Char Kway Teow", value: 33, color: "#d24d57"},
				{label: "Ban Mian", value: 33, color: "#dcc6e0"},
			];
		};
		$scope.revenue_options = {thickness: 70};
		$scope.transactions = [
			{
				payer: "86457213",
				payment: "dbs paylah!",
				amount: "$5.50",
				order: "Bee Hoon",
				status: "fulfilled",
				url: "/transaction/123",
			},{
				payer: "977652435",
				payment: "dbs paylah!",
				amount: "$4.50",
				order: "Hokkien Mee",
				status: "pending",
				url: "/transaction/123",
			},{
				payer: "87654832",
				payment: "cash",
				amount: "$4.50",
				order: "Hokkien Mee",
				status: "cancelled",
				url: "/transaction/123",
			},{
				payer: "86457213",
				payment: "dbs paylah!",
				amount: "$5.50",
				order: "Bee Hoon",
				status: "fulfilled",
				url: "/transaction/123",
			},{
				payer: "977652435",
				payment: "dbs paylah!",
				amount: "$4.50",
				order: "Hokkien Mee",
				status: "pending",
				url: "/transaction/123",
			},{
				payer: "87654832",
				payment: "cash",
				amount: "$4.50",
				order: "Hokkien Mee",
				status: "fulfilled",
				url: "/transaction/123",
			},{
				payer: "86457213",
				payment: "dbs paylah!",
				amount: "$5.50",
				order: "Bee Hoon",
				status: "fulfilled",
				url: "/transaction/123",
			},{
				payer: "977652435",
				payment: "dbs paylah!",
				amount: "$4.50",
				order: "Hokkien Mee",
				status: "fulfilled",
				url: "/transaction/123",
			},{
				payer: "87654832",
				payment: "cash",
				amount: "$4.50",
				order: "Hokkien Mee",
				status: "fulfilled",
				url: "/transaction/123",
			},{
				payer: "86457213",
				payment: "dbs paylah!",
				amount: "$5.50",
				order: "Bee Hoon",
				status: "fulfilled",
				url: "/transaction/123",
			},{
				payer: "977652435",
				payment: "dbs paylah!",
				amount: "$4.50",
				order: "Hokkien Mee",
				status: "fulfilled",
				url: "/transaction/123",
			},{
				payer: "87654832",
				payment: "cash",
				amount: "$4.50",
				order: "Hokkien Mee",
				status: "fulfilled",
				url: "/transaction/123",
			},
		];
	});
	app.controller("HistoryCtrl", function($scope) {
		$scope.name = "App Transaction History Controller";
		$scope.initHistory = function() {
			
		};
	});
	app.controller("OrderCtrl", function($scope) {
		$scope.name = "App Order Status Controller";
		$scope.initOrder = function() {
			
		};
	});
})();
