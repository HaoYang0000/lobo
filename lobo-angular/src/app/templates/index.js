import angular from 'angular';
import { HomeComponent } from './Main/main.js';
import { InboxComponent } from './Inbox/inbox.js';
import {GuidesComponent} from "./Guides/guides";
import {GuideComponent} from "./Guide/guide";
import {ConversationCardComponent} from "./ConversationCard/conversation-card";
import {GuideCardComponent} from "./GuideCard/guide-card";
import {ConversationComponent} from "./Conversation/conversation";

export default angular.module('lobo.components', [])
    .component('loboHome', HomeComponent.create())
    .component('loboInbox', InboxComponent.create())
    .component('loboGuides', GuidesComponent.create())
    .component('loboGuide', GuideComponent.create())
    .component('loboConvCard', ConversationCardComponent.create())
    .component('loboGuideCard', GuideCardComponent.create())
    .component('loboConversation', ConversationComponent.create())
    .name;
