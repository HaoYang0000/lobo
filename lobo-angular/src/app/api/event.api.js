export default class EventApi {
    constructor (Restangular) {
        this.rest = Restangular.service('user_events');
    }
    list () {

    }
    async retrieve (eventId, route) {
        let req = this.rest.one(eventId);
        if (route) {
            req = req.one(route);
        }
        let res = await req.get();
        return res.plain();
    }
    create () {

    }
}
