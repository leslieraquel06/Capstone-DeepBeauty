// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { RouterModule } from '@angular/router';
import { HometabComponent } from './hometab/hometab.component'; // Import your components here
import { ProducttabComponent } from './producttab/producttab.component';
import { CommunitytabComponent } from './communitytab/communitytab.component';
import { QuiztabComponent } from './quiztab/quiztab.component';

@NgModule({
  declarations: [
    AppComponent, 
    HometabComponent, // Include your components here
    ProducttabComponent,
    CommunitytabComponent,
    QuiztabComponent
  ],
  imports: [
    BrowserModule, RouterModule.forRoot([]),AppRoutingModule
  ],
  bootstrap: [AppComponent] // Add AppComponent to the bootstrap array
})

export class AppModule { }
