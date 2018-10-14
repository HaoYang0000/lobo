export class ConversationCardComponent {
    constructor ($scope, UserApi) {
        this.UserApi = UserApi;
        this.$scope = $scope;
    }
    $onInit ($scope) {
        this.UserApi.retrieve(this.convo.id).then((user)=>{
            this.convo.user=user;
            this.$scope.$apply();
            console.log(this.convo)
        })

    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
                convo:'=',
            },
            controller: ConversationCardComponent,
            template: require('./conversation-card.html')
        };
    }
}
