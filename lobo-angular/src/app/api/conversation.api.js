
export default class ConversationApi {
    constructor(Restangular) {
        this.rest = Restangular.service('conversations');

    }

    async list(params) {
        console.log('Listing guides. Query params==', params);
        let res = await this.rest.get('', params);
        console.log(res.plain());
        return res.plain();
    }

    async retrieve(userId, route) {
        let req = this.rest.one(userId)
        if (route) {
            req = req.one(route)
        }
        let res = await req.get();
        return res.plain();
    }
    async push(message){
        let req = await this.rest.post(message)
        return req.plain();
    }
}
