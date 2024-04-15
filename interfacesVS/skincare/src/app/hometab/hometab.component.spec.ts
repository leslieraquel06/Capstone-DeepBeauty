import { ComponentFixture, TestBed } from '@angular/core/testing';

// Import the component to be tested
import { HometabComponent } from './hometab.component';

describe('HometabComponent', () => {
  let component: HometabComponent;
  let fixture: ComponentFixture<HometabComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [HometabComponent] // Declare HometabComponent as a dependency
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(HometabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

