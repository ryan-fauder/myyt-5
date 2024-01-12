import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdicionarVideoComponent } from './adicionar-video.component';

describe('AdicionarVideoComponent', () => {
  let component: AdicionarVideoComponent;
  let fixture: ComponentFixture<AdicionarVideoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdicionarVideoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdicionarVideoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
