
export class AppointmentCardComponent {
    constructor ($scope,UserApi,EventApi) {
        this.$scope=$scope;
        this.UserApi = UserApi;
        this.EventApi = EventApi;
    }
    $onInit () {
        console.log(this.event)
        this.event.date = new Date(this.event.created_at);
        this.EventApi.retrieve(this.event.id).then(({user_id_two})=>{
            console.log(user_id_two)
            this.UserApi.retrieve(user_id_two).then(user=>{
                this.event.guide = user;
            })
        })
    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
                event:'=',
            },
            controller: AppointmentCardComponent,
            template: require('./appointment-card.html')
        };
    }
}
