import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { FormsModule } from '@angular/forms';

import { NewProjectComponent } from './new-project.component';

describe('NewProjectComponent', () => {
  let component: NewProjectComponent;
  let fixture: ComponentFixture<NewProjectComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NewProjectComponent ],
      imports: [HttpClientTestingModule, FormsModule]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NewProjectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
