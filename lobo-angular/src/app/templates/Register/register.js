export class RegisterComponent {
    constructor (UserApi, $state, $stateParams) {
        console.log($state, $stateParams);
        if ($stateParams.loginError) {
            this.showErrorModal();
        }
        this.$state = $state;
        this.api = UserApi;
        this.loginForm = {};
        // $('#usernameInput').keyup(function () {
        //     $(this).val($(this).val().replace(/(\d{3})\-?(\d{3})\-?(\d{4})/, '$1-$2-$3'));
        // });
    }
    async register () {
        try {
            let res = await this.api.register(this.loginForm);
            console.log('got register response', res);
            if (!res) {
                throw new Error('login error');
            }
            this.loginSuccessful = true;
            this.$state.transitionTo('login');
        } catch (err) {
            console.error('Login Error', err);
            this.loginError = true;
            this.showErrorModal();
        }
    }
    showErrorModal () {
        this.modal.show();
        // angular.element('#loginErrorModal')
        this.modal.on('shown.bs.modal', () => {
            this.modal.trigger('focus');
        });
    }
    get modal () {
        return angular.element('#loginErrorModal');
    }
    hideModal () {
        console.log('hiding modal', angular.elemen);
        this.modal.hide();
    }
    static create () {
        return {
            bindings: {
                registerError: '='
            },
            controller: RegisterComponent,
            template: require('./register.html')
        };
    }
}
