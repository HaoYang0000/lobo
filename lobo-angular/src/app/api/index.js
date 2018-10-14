import angular from 'angular';
import restangular from 'restangular';
import RestConfig from './config.js';
import UserApi from './user.api.js';
import ConversationApi from './conversation.api.js';
import EventApi from './event.api.js';
import ReviewApi from './review.api.js';
import ServiceApi from './service.api.js';
export default angular.module('lobo.api', [restangular])
    .config(RestConfig)
    .service('UserApi', UserApi)
    .service('ConversationApi', ConversationApi)
    .service('EventApi', EventApi)
    .service('ReviewApi', ReviewApi)
    .service('ServiceApi', ServiceApi)
    .name;
