'use strict';
import angular from 'angular';
import ngAnimate from 'angular-animate';
import LoboConfig from './config';
import LoboApi from './api';
import LoboComponents from './templates';

import '../style/app.css';

const MODULE_NAME = 'app';

export default angular.module(MODULE_NAME,
    [
        ngAnimate,
        LoboConfig,
        LoboComponents,
        LoboApi
    ]
);
