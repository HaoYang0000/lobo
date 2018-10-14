
export class GuideRequestComponent {
    constructor (UserApi,$stateParams,$scope,$state) {
        $scope.backHref=$state.href('guides.profile');
        $scope.setups = {
            days:[],

            years:[],
        };
        $scope.event = {
          date:{
              month:"",
              day:"",
              year:"",
          },
          time:{
              timeOfDay:'AM',
          },
        };
        for (var i = 1;i<=31;i++){
            $scope.setups.days.push(i)
        }
        $scope.schedule = () =>{
            console.log($scope.event)
        }
    }
    $onInit () {
        console.log(this)
    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
            },
            controller: GuideRequestComponent,
            template: require('./guide-request.html')
        };
    }
}
