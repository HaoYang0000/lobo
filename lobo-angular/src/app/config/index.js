import angular from 'angular';
import restangular from 'restangular';
import uiRouter from '@uiRouter/angularjs';
import RestConfig from './rest.config.js';
import StateConfig from './state.config.js';
import RouteConfig from './route.config.js';

export default angular.module('lobo.config',
    [
        restangular,
        uiRouter
    ]
)
    .config(RestConfig)
    .config(StateConfig)
    .config(RouteConfig).name;
