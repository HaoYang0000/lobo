import angular from 'angular';
import { HomeComponent } from './Main/main.js';
import { InboxComponent } from './Inbox/inbox.js';
import {GuidesComponent} from "./Guides/guides";

export default angular.module('lobo.components', [])
    .component('loboHome', HomeComponent.create())
    .component('loboInbox', InboxComponent.create())
    .component('loboGuides', GuidesComponent.create())
    .name;
