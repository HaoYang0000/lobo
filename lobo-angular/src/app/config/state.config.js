export default function StateConfig ($stateProvider) {
    $stateProvider.state(
        {
            name: 'home',
            url: '/',
            template: '<lobo-home/>',
        }
    ).state(
        {
            name: 'home.inbox',
            url: '/inbox/',
            template: '<lobo-inbox/>'
        }
    ).state(
        {
            name: 'home.guides',
            url:'/',
            template: '<lobo-guides/>'
        }
    );
}
