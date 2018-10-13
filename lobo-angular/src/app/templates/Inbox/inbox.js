export class InboxComponent {
    constructor () {
        console.log('Yoooo');
    }
    $onInit () {

    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
            },
            controller: InboxComponent,
            template: require('./inbox.html')
        };
    }
}
