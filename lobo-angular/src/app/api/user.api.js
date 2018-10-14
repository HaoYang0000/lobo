
export default class UserApi {
    constructor (Restangular, $timeout) {
        this.$timeout = $timeout;
        this.Restangular = Restangular;
        this.rest = Restangular.service('users');
        this.auth = Restangular.service('auth');
    }
    async list (params) {
        console.log('Listing guides. Query params==', params);
        let res = await this.rest.get('', params);
        console.log(res.plain());
        return res.plain();
    }
    async retrieve (userId, route) {
        let req = this.rest.one(userId);
        if (route) {
            req = req.one(route);
        }
        let res = await req.get();
        return res.plain();
    }
    set token (token) {
        this.Restangular.configuration.defaultHeaders = {
            'Authentication': token
        };
        this._token = token;
    }
    get token () {
        return this._token;
    }
    set data (data) {
        if ('jwt' in data) {
            this.token = data.jwt;
        }
        this._data = data;
    }
    get data () {
        return this._data;
    }
    async login (login) {
        console.log(login.username, login.password);
        let userdata = await this.auth.post({
            'phone': login.username,
            'password': login.password
        });
        this.data = userdata;
        return userdata;
    }
    async register (registerData) {
        let data = await this.$timeout(
            (registerData) => {
                if (registerData.demo) {
                    return this.login({ phone: '3140000000', password: 'catgif' });
                }
                console.log('Registration complete');
                return this.login({ phone: '3140000000', password: 'catgif' });
            }, 1000);
        console.log(data);
        return data;
        // let registerData = await this.users.post(data);
    }
}
