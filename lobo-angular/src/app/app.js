'use strict';
import angular from 'angular';
import LoboConfig from './config';
import LoboApi from './api';
import LoboComponents from './templates';

import '../style/app.css';

const MODULE_NAME = 'app';

export default angular.module(MODULE_NAME,
    [
        LoboConfig,
        LoboComponents,
        LoboApi
    ]
);
