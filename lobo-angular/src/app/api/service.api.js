/*
General
    Get a driver's license
    Register my vehicle
    Navigate public transportation
    Share local restaurants
Money
    Open a bank account
    Open a credit card
    Understand my medical bill
    Understand my electricity bill
Information Technology Professionals
    Resume assistance
    Networking
    Skill transferability
Medical Professionals
    Resume assistance
    Networking
    Skill transferability
Entrepreneurship
    Legal Assistance
    Marketing
    */
export default class ServiceApi {
    constructor (Restangular) {
        this.rest = Restangular.service('services');
    }
    list (params) {
        this.rest.get(params);
    }
    retrieve (serviceType) {
        this.rest.one(serviceType).get();
    }
    create () {
    }

}
