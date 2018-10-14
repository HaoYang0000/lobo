import UserApi from "../../api/user.api";

export class GuidesComponent {
    constructor (UserApi, $timeout,$scope) {
        this.api = UserApi;
        this.api.list().then((guides)=>{
            $scope.guides= guides;
            $scope.$apply();
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
            controller: GuidesComponent,
            template: require('./guides.html')
        };
    }
}
