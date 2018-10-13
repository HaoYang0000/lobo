import angular from 'angular';
import { HomeComponent } from './Main/main.js';

export default angular.module('lobo.components', [])
    .component('loboHome', HomeComponent.create())
    .name;
