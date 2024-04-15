import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HometabComponent } from './hometab/hometab.component';
import { CommunitytabComponent } from './communitytab/communitytab.component';
import { ProducttabComponent } from './producttab/producttab.component';
import { QuiztabComponent } from './quiztab/quiztab.component';

const routes: Routes = [
  { path: '', redirectTo: '/hometab', pathMatch: 'full' },
  { path: 'hometab', component: HometabComponent },
  { path: 'communitytab', component: CommunitytabComponent },
  { path: 'producttab', component: ProducttabComponent },
  { path: 'quiztab', component: QuiztabComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

