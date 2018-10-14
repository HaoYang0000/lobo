
export class GuideProfileComponent {
    constructor (UserApi,$stateParams,$scope,$state) {
        console.log($scope)
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
