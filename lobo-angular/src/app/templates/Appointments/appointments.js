
export class AppointmentsComponent {
    constructor ($scope, UserApi) {
        this.UserApi = UserApi;
        this.userId = 1;
        $scope.events = [];
        this.UserApi.retrieve(this.userId,'events').then((events)=>{
            $scope.events = events;
            $scope.$apply();
        })
    }
    $onInit () {

    }
    $onDestroy () {

    }
    static create () {
        return {
            controller: AppointmentsComponent,
            template: require('./appointments.html')
        };
    }
}
