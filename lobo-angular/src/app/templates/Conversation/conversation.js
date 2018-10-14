export class ConversationComponent {
    constructor () {
    }
    $onInit () {
        console.log('this ids')
    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
            },
            controller: ConversationComponent,
            template: require('./conversation.html')
        };
    }
}
