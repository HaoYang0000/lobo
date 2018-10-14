
export class HomeComponent {
    constructor (UserApi) {
        console.log('home component');

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
