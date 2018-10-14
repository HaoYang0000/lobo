export class RegisterComponent {
    constructor (UserApi, $state, $stateParams, $timeout) {
        console.log($state, $stateParams);
        if ($stateParams.loginError) {
            this.showErrorModal();
        }
        this.$timeout = $timeout;
        this.$state = $state;
        this.api = UserApi;
        this.step = 1;
        this.langs = [
            'English',
            'Russion',
            'Spanish',
            'French',
            'Arabic',
            'Mandarin',
            'Hindi',
            'Japanese'
        ];
        // $('#usernameInput').keyup(function () {
        //     $(this).val($(this).val().replace(/(\d{3})\-?(\d{3})\-?(\d{4})/, '$1-$2-$3'));
        // });
    }
    $onInit () {
        this.registerForm = {};
    }
    isComplete () {
        let c = !!(this.registerForm.firstname && this.registerForm.lastname && this.registerForm.phone);
        console.log(c);
        return c;
    }
    async register () {
        try {
            this.submitted = true;
            let res = await this.api.register(this.registerForm);
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
    set step (step) {
        this._step = step;
    }
    get step () {
        return this._step;
    }
    setStep (step) {
        this.step = 0;
        this.$timeout(() => {
            this.step = step;
        }, 500);
    }
    setLang (lang) {
        if (this.langs.includes(lang)) {
            this.registerForm.lang = lang;
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
        return angular.element('#registerErrorModal');
    }
    hideModal () {
        this.modal.hide();
        this.setStep(1);
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
