import UserApi from "../../api/user.api";
export class GuideComponent {
    constructor (UserApi,$stateParams,$scope,$state) {
        console.log($stateParams)
        this.userId=$stateParams.userId;
        this.api = UserApi;
        this.api.retrieve(this.userId).then((data)=>{
            this.guide = data;
            $scope.guide = data;
            $scope.$apply();
            $state.go('guide.profile',{guide:this.guide});
            $scope.$state = $state;
        }).catch((err)=>{
            console.log(err);
        });
    }
    $onInit () {

    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
            },
            controller: GuideComponent,
            template: require('./guide.html')
        };
    }
}
