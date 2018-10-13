
export class HomeComponent {
    constructor (UserApi) {



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
            template: require('./main.html')
        };
    }
}
