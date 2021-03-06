import angular from 'angular';
import { HomeComponent } from './Home/home.js';
import { InboxComponent } from './Inbox/inbox.js';


import {GuidesComponent} from "./Guides/guides";
import {GuideComponent} from "./Guide/guide";
import {GuideRequestComponent} from "./GuideRequest/guide-request";
import {ConversationCardComponent} from "./ConversationCard/conversation-card";
import {GuideCardComponent} from "./GuideCard/guide-card";
import {GuideProfileComponent} from "./GuideProfile/guide-profile";
import {ConversationComponent} from "./Conversation/conversation";
import {MessageComponent} from "./Message/message";
import { LoginComponent } from './Login/login';
import { RegisterComponent } from './Register/register';
import { AppointmentsComponent } from './Appointments/appointments';
import { AppointmentCardComponent } from './AppointmentCard/appointment-card';


export default angular.module('lobo.components', [])
    .component('loboHome', HomeComponent.create())
    .component('loboLogin', LoginComponent.create())
    .component('loboRegister', RegisterComponent.create())
    .component('loboInbox', InboxComponent.create())
    .component('loboGuides', GuidesComponent.create())
    .component('loboConvCard', ConversationCardComponent.create())
    .component('loboGuide', GuideComponent.create())
    .component('loboGuideCard', GuideCardComponent.create())
    .component('loboGuideRequest', GuideRequestComponent.create())
    .component('loboGuideProfile', GuideProfileComponent.create())
    .component('loboConversation', ConversationComponent.create())
    .component('loboMessage', MessageComponent.create())
    .component('loboAppointments', AppointmentsComponent.create())
    .component('loboAppointmentCard', AppointmentCardComponent.create())
    .name;
