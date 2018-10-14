export class GuideCardComponent {
    constructor ($scope) {
    }
    $onInit () {

    }
    $onDestroy () {

    }
    static create () {
        return {
            bindings: {
                guide: '='
            },
            controller: GuideCardComponent,
            template: require('./guide-card.html')
        };
    }
}
