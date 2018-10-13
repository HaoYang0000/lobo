import angular from 'angular';
import restangular from 'restangular';
import uiRouter from '@uiRouter/angularjs';
import StateConfig from './state.config.js';
import RouteConfig from './route.config.js';

export default angular.module('lobo.config',
    [
        restangular,
        uiRouter
    ]
)
    .config(StateConfig)
    .config(RouteConfig).name;
