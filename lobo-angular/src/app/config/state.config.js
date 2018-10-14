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
        ).state('home.inbox',
        {
            url: '^/inbox/',
            views: {
                'center@home': {
                    template: '<lobo-inbox/>'
                }
            }
        }
    ).state('home.guides',
        {
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
    ).state('guide.profile',
        {


            views: {
                'guideContent@guide': {
                    template: '<lobo-guide-profile/>'
                }
            }
        }
    ).state('guide.request',
        {

            views: {
                'guideContent@guide': {
                    template: '<lobo-guide-request/>'
                }
            }
        }
        ).state('conversation',
        {
            name: 'conversation',
            url: '^/conversation/:userId',
            views: {
                'index': {
                    template: '<lobo-conversation/>'
                }
            }
        }
    ).state('login',
        {
            name: 'login',
            url: '^/login/',
            views: {
                'index': {
                    template: '<lobo-login/>'
                }
            }
        });




}
