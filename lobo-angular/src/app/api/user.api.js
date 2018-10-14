
export default class UserApi {
    constructor (Restangular) {
        this.rest = Restangular.service('users');
        this.auth = Restangular.service('auth');
    }
    async list (params) {
        console.log('Listing guides. Query params==', params);
        let res = await this.rest.get('', params);
        console.log(res.plain());
        return res.plain();
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
