export default function StateConfig ($stateProvider) {
    $stateProvider
        .state('home',
            {
                name: 'home',
                url: '^/',
                views: {
                    'index': {
                        template: '<lobo-home/>'
                    }
                },
                resolve: {
                    login: function ($q, $state) {
                        let deferred = $q.defer();
                        console.log('eat some shit');
                        return true;
                    }
                }
            }
        ).state('inbox',
            {
                parent: 'home',
                url: '^/inbox/',
                views: {
                    'center@home': {
                        template: '<lobo-inbox/>'
                    }
                }
            }
        ).state('guides',
            {
                parent: 'home',
                name: 'home.guides',
                url: '^/guides/',
                views: {
                    'center@home': {
                        template: '<lobo-guides/>'
                    }
                }
            }
        ).state('guide',
            {
                name: 'guide',
                url: '^/guide/:userId/',
                views: {
                    'index': {
                        template: '<lobo-guide/>'
                    }
                }
            }
        ).state('conversation',
            {
                name: 'conversation',
                url: '^/conversation/',
                views: {
                    'index': {
                        template: '<lobo-conversation/>'
                    }
                }
            }
        );
}
