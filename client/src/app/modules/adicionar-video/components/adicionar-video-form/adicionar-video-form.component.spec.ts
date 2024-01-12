import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdicionarVideoFormComponent } from './adicionar-video-form.component';

describe('AdicionarVideoFormComponent', () => {
  let component: AdicionarVideoFormComponent;
  let fixture: ComponentFixture<AdicionarVideoFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdicionarVideoFormComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdicionarVideoFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
