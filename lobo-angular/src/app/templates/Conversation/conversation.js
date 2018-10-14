export class ConversationComponent {
    constructor ($stateParams,$scope,ConversationApi) {

        $scope.convo = $stateParams.convo;
        this.ConversationApi = ConversationApi;
        this.userId = 1;
        $scope.sendMessage = () =>{
            if($scope.entry){
                const message = {
                    content:$scope.entry,
                    user_id_one:this.userId,
                    user_id_two:$scope.convo.user.id,
                    is_read:false,
                }
                this.ConversationApi.push(message)
                $scope.convo.messages.push(message)
                $scope.entry="";
            }
        }
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
