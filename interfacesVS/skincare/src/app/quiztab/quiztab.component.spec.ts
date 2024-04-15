import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuiztabComponent } from './quiztab.component';

describe('QuiztabComponent', () => {
  let component: QuiztabComponent;
  let fixture: ComponentFixture<QuiztabComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [QuiztabComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(QuiztabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
