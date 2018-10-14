
export class GuideRequestComponent {
    constructor (UserApi,$stateParams,$scope,$state) {
        $scope.backHref=$state.href('guides.profile');
    }
    $onInit () {
        console.log(this)
    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
            },
            controller: GuideRequestComponent,
            template: require('./guide-request.html')
        };
    }
}
