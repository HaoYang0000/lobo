export class ConversationComponent {
    constructor () {
        console.log('conversation component', 'this ids');
    }
    $onInit () {

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
