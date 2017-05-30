import {  ApplicationRef, Component, Injector, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule, Router } from '@angular/router';
import { DynamicFormControlModel, DynamicFormService, DynamicCheckboxModel, DynamicInputModel,    DynamicSelectModel,DynamicTextAreaModel, } from '@ng2-dynamic-forms/core';


import { EntityConfigComponent } from '../../../common/entity/entity-config/';
import { GlobalState } from '../../../../global.state';
import { RestService, WebSocketService, UserService } from '../../../../services/';
import * as _ from 'lodash';

import { Subscription } from 'rxjs';

@Component ({
    selector: 'afp-edit',
    template: ` <entity-config [conf]="this"></entity-config>`,
    providers: [UserService]
})

export class ServiceFTPComponent {
  protected resource_name: string = 'services/ftp';
  private entityEdit: EntityConfigComponent;
  protected route_success: string[] = ['services'];

  protected formModel: DynamicFormControlModel[] = [
    new DynamicCheckboxModel({
      id: 'ftp_anonuserbw',
      label: 'Guest Access',
    }),
    new DynamicSelectModel({
      id: 'ftp_ident',
      label: 'Guest Account',
    }),
    new DynamicInputModel({
        id: 'ftp_timeout',
        label: 'Max. Connections',
    }),
    new DynamicCheckboxModel({
      id: 'ftp_resume',
      label: 'Enable home directories',
    }),
   new DynamicInputModel({
      id: 'ftp_options',
      label: 'Home Directories',
    }),
    new DynamicInputModel({
      id: 'ftp_masqaddress',
      label: 'Home share name',
    }),
   new DynamicInputModel({
      id: 'afp_srv_dbpath',
      label: 'Database Path',
    }),
   new DynamicTextAreaModel({
      id: 'afp_srv_global_aux',
      label: 'Global auxiliary parameters',
    }),
    new DynamicSelectModel({
        id: 'afp_srv_chmod_request',
        label: 'Chmod Request',
        options: [
          { label: 'Ignore', value: 'ignore' },
          { label: 'Preserve', value: 'preserve' },
          { label: 'Simple', value: 'simple' },
        ],
    }),
    new DynamicSelectModel({
        id: 'afp_srv_map_acls',
        label: 'Map ACLs',
        options: [
          { label: 'Rights', value: 'rights' },
          { label: 'None', value: 'none' },
          { label: 'Mode', value: 'mode' },
        ],
    }),
    new DynamicInputModel({
        id: 'afp_srv_bindip',
        label: 'Bind Interfaces',
    }),
  ];
  
  constructor(protected router: Router, protected route: ActivatedRoute, protected rest: RestService,  protected ws: WebSocketService, protected formService: DynamicFormService,  protected _injector: Injector, protected _appRef: ApplicationRef,   protected _state: GlobalState, protected userService: UserService) {

  }

  afterInit(entityEdit: any) {
    this.entityEdit = entityEdit;
  }

}


