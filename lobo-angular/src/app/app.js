'use strict';
import angular from 'angular';
import LoboConfig from './config';
import LoboComponents from './templates';

import '../style/app.css';

let app = () => {
    return {

        // template: require('./app.html'),
        template: require('./main.html'),
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

export default angular.module(MODULE_NAME,
    [
        LoboConfig,
        LoboComponents
    ]
)
    .directive('app', app)
    .controller('AppCtrl', AppCtrl)
    .service('Api', ApiService);
