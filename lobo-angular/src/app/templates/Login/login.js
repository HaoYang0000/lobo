const target = {};
const loginProxy = new Proxy(target, {
    get: (target, name) => {
        return target[name];
    },
    set: (target, name, value) => {
        target[name] = value;
    }
});
export class LoginComponent {
    constructor (UserApi) {
        this.api = UserApi;
        this.loginForm = new Proxy(target, {
            get: (t, n) => {

            },
            set: (t, n, v) => {
                t[n] = v;
            }
        });
        // $('#usernameInput').keyup(function () {
        //     $(this).val($(this).val().replace(/(\d{3})\-?(\d{3})\-?(\d{4})/, '$1-$2-$3'));
        // });
    }
    async login () {
        try {
            let res = await this.api.login(loginProxy);
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
