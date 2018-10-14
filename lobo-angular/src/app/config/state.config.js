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
            url: '/',
            template: '<lobo-inbox/>'
        }
    ).state(
        {
            name: 'home.guides',
            url:'/',
            template: '<lobo-guides/>'
        }
    ).state(
        {
            name: 'guide',
            url:'/guide/:userId',
            template: '<lobo-guide/>'
        }
    ).state(
        {
            name: 'conversation',
            // url:'/conversation/:conversationId',
            url:'/',
            template: '<lobo-guide/>'
        }
    );
}
