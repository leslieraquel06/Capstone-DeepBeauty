// app.module.ts

import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { SharedModule } from './shared.module';

@NgModule({
  declarations: [AppComponent, ],
  imports: [BrowserModule, SharedModule],
  bootstrap: [AppComponent]
})
export class AppModule {}


