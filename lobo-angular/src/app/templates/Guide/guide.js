import UserApi from "../../api/user.api";
export class GuideComponent {
    constructor (UserApi,$stateParams,$scope) {
        console.log($stateParams)
        this.userId=$stateParams.userId;
        this.api = UserApi;
        this.api.retrieve(this.userId).then((data)=>{
            this.guide = data;
            $scope.guide = data;
            $scope.$apply();
        }).catch((err)=>{
            console.log(err);
        });
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
            controller: GuideComponent,
            template: require('./guide.html')
        };
    }
}
