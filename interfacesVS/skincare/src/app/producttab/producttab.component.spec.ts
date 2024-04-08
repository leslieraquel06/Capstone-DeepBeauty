import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProducttabComponent } from './producttab.component';

describe('ProducttabComponent', () => {
  let component: ProducttabComponent;
  let fixture: ComponentFixture<ProducttabComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProducttabComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ProducttabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
