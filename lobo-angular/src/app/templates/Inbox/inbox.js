
export class InboxComponent {
    constructor (ConversationApi,UserApi,$scope) {
        console.log('Yoooo');
        const userId=1;
        this.ConversationApi = ConversationApi;
        this.UserApi = UserApi;
        $scope.convos = [];
        this.ConversationApi.retrieve(userId).then((messages)=>{

            angular.forEach(messages,async (message)=>{
                message.formattedDate = new Date(message.created_at)
                const otherUser = message.user_id_one!=userId?message.user_id_one:message.user_id_two;
                const convoIds = $scope.convos.map((convo)=>{
                    return convo.id;
                })

                let convoIndex = convoIds.indexOf(otherUser);

                if (convoIndex==-1){


                     convoIndex = $scope.convos.push({

                         id:otherUser,
                         messages:[],
                     })-1;
                }
                $scope.convos[convoIndex].messages.push(message)
            })
            $scope.$apply();
        })
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
