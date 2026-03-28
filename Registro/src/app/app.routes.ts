import { Routes } from '@angular/router';
import { DocenteComponent } from './docente/docente';
import { StudenteComponent } from './studente/studente';
import { docenteGuard } from './docente-guard';
import { studenteGuard } from './studente-guard';
import { AccessoNegato } from './accesso-negato/accesso-negato';

export const routes: Routes = [
    

{
path:'docente',
component:DocenteComponent,
canActivate:[docenteGuard]
},

{
path:'studente',
component:StudenteComponent,  
canActivate:[studenteGuard]
},

{
path:'accesso-negato',
component:AccessoNegato
}


];
