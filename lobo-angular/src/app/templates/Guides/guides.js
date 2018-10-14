import UserApi from '../../api/user.api';

export class GuidesComponent {
    constructor (UserApi, $timeout, $scope) {
        console.log('Guides component');
        this.api = UserApi;
        this.api.list().then((guides) => {
            $scope.guides = guides;
            console.log($scope);
            $scope.$apply();
        }).catch((err) => {
            console.log(err);
        });
    }
    $onInit () {

    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
            },
            controller: GuidesComponent,
            template: require('./guides.html')
        };
    }
}
