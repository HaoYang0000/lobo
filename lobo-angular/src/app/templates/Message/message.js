
export class MessageComponent {
    constructor ($scope) {
        this.$scope=$scope;
    }
    $onInit () {
        this.userId = 1;
        console.log(MessageComponent)
        this.$scope.isSender = this.userId==this.message.user_id_one;
    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
                message:'=',
            },
            controller: MessageComponent,
            template: require('./message.html')
        };
    }
}
