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
    }
    login () {
        this.api.login(loginProxy);
    }
    register () {
        // If we want to add a register page
    }
    static create () {
        return {
            bindings: {},
            controller: LoginComponent,
            template: require('./login.js')
        };
    }
}
