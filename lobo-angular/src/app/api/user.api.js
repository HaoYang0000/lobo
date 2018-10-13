export default class UserApi {
    constructor (Restangular) {
        this.rest = Restangular.service('users');
        this.auth = Restangular.service('auth');
    }
    list (params) {
        return this.rest.get(params);
    }
    retrieve (userId) {
        return this.rest.one(userId).get();
    }
    login (login) {
        return this.auth.post(undefined, {
            'user_name': login.username,
            'password': login.password
        });
    }
}
