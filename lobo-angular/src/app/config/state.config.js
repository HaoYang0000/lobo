export default function StateConfig ($stateProvider) {
    $stateProvider.state(
        {
            name: 'home',
            url: '/',
            template: '<lobo-home/>'
        },
        {
            name: 'inbox',
            url: '/inbox',
            template: '<lobo-index/>'
        }
    );
}
