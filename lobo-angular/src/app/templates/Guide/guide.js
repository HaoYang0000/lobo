export class GuideComponent {
    constructor () {
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
