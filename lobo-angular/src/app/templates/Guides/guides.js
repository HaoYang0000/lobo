import UserApi from '../../api/user.api';

export class GuidesComponent {
    constructor (UserApi, $timeout, $scope) {

        this.api = UserApi;
        $scope.services = [];
        this.api.list().then((guides) => {
            $scope.guides = guides;
           angular.forEach(guides,(guide)=>{
                this.api.retrieve(guide.id,'services').then((services)=>{
                    angular.forEach(services,(service)=>{
                       const currentIds = $scope.services.map((currentService)=>{
                           return currentService.id
                       })

                        let currentIndex = currentIds.indexOf(service.id);
                        if(currentIndex==-1){
                            currentIndex = $scope.services.push(service)-1;
                        }
                        if($scope.services[currentIndex].guides ===undefined){
                            $scope.services[currentIndex].guides = []
                        }
                        let new_guide = Object.assign({},guide);
                        new_guide.is_expert  = service.is_expert;
                        $scope.services[currentIndex].guides.push(new_guide);
                    });
                });
            })
            $scope.$apply();
        }).catch((err) => {
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
