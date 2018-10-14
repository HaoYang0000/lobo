
export class GuideProfileComponent {
    constructor (UserApi,$stateParams,$scope,$state) {
        $scope.backHref=$state.href('home.guides');
        console.log($scope.backHref)
    }
    $onInit () {

    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
            },
            controller: GuideProfileComponent,
            template: require('./guide-profile.html')
        };
    }
}
