export class LoginComponent {
    constructor (UserApi, $state) {
        if (this.loginError) {
            //If we resolve unautheticated views to go back
        }
        this.$state = $state;
        this.api = UserApi;
        this.loginForm = {};
        // $('#usernameInput').keyup(function () {
        //     $(this).val($(this).val().replace(/(\d{3})\-?(\d{3})\-?(\d{4})/, '$1-$2-$3'));
        // });
    }
    async login () {
        try {
            let res = await this.api.login(this.loginForm);
            console.log('got auth response', res);
            if (!res) {
                throw new Error('login error');
            }
            this.loginSuccessful = true;
            this.$state.transitionTo('home');
        } catch (err) {
            console.error('eat som shyit', err);
            this.loginError = true;
            this.showErrorModal();
        }
    }
    register () {
        // If we want to add a register page
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
                loginError: '='
            },
            controller: LoginComponent,
            template: require('./login.html')
        };
    }
}
