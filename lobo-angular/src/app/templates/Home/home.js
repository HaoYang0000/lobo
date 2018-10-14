
export class HomeComponent {
    constructor (UserApi,$state) {
        console.log('home component');
        $state.go('home.guides')
    }
    $onInit () {

    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
            },
            controller: HomeComponent,
            template: require('./home.html')
        };
    }
}
