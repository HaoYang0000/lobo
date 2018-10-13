import angular from 'angular';
import restangular from 'restangular';
import RestConfig from './config/rest.js';

import '../style/app.css';

let app = () => {
    return {

        // template: require('./app.html'),
        template: require('./templates/Main/main.html'),
        controller: 'AppCtrl',
        controllerAs: 'app'
    };
};

class AppCtrl {
    constructor (Api) {
        this.url = 'https://github.com/preboot/angular-webpack';
        this.api = Api;
    }
}
class ApiService {
    constructor (Restangular, $log) {

        this.$log = $log;
        this.Restangular = Restangular;
    }
    users (uuid) {
        this.$log.debug('Hey!');
        return this.Restangular.one('users', uuid).get();
    }
}

const MODULE_NAME = 'app';

angular.module(MODULE_NAME, [restangular]).directive('app', app).controller('AppCtrl', AppCtrl);

angular.module(MODULE_NAME).service('Api', ApiService);

angular.module(MODULE_NAME).config(RestConfig);

export default MODULE_NAME;
