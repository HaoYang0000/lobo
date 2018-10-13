import angular from 'angular';
import restangular from 'restangular';

import '../style/app.css';

let app = () => {
  return {
    template: require('./app.html'),
    controller: 'AppCtrl',
    controllerAs: 'app'
  }
};

class AppCtrl {
  constructor(Api) {
    this.url = 'https://github.com/preboot/angular-webpack';
    this.api = Api;
  }
}
class ApiService{
    constructor(Restangular, $log){
        this.$log = $log;
        this.Restangular = Restangular;
    }
    users(uuid){
        this.$log.debug('Hey!');
        return this.Restangular.one('users', uuid).get();
    }
}
class RestConfig{
    constructor(RestangularProvider) {
    RestangularProvider.setBaseUrl('localhost:8732/api/v1');
}
}
const MODULE_NAME = 'app';

angular.module(MODULE_NAME, [restangular]).directive('app', app).controller('AppCtrl', AppCtrl);

angular.module(MODULE_NAME).service('Api', ApiService);



export default MODULE_NAME;
