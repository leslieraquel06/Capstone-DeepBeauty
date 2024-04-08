import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CommunitytabComponent } from './communitytab.component';

describe('CommunitytabComponent', () => {
  let component: CommunitytabComponent;
  let fixture: ComponentFixture<CommunitytabComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CommunitytabComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CommunitytabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
