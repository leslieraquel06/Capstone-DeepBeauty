import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-producttab',
  standalone: true,
  templateUrl: './producttab.component.html',
  styleUrl: './producttab.component.css',
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive]
})
export class ProducttabComponent {

}
