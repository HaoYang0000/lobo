export class LoginComponent {
    constructor (UserApi) {
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
        } catch (err) {
            console.error(err);
        }
    }
    register () {
        // If we want to add a register page
    }
    static create () {
        return {
            bindings: {},
            controller: LoginComponent,
            template: require('./login.html')
        };
    }
}
