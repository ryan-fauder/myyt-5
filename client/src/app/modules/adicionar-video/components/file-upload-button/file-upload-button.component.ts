import { FocusMonitor } from '@angular/cdk/a11y';
import { BooleanInput, coerceBooleanProperty } from '@angular/cdk/coercion';
import { HttpClient, HttpEventType } from '@angular/common/http';
import { Component, ElementRef, EventEmitter, HostBinding, Input, OnDestroy, Optional, Output, Self, forwardRef } from '@angular/core';
import { AbstractControlDirective, ControlValueAccessor, FormControl, NG_VALUE_ACCESSOR, NgControl, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldControl, MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { Observable, Subject, Subscription, finalize } from 'rxjs';

@Component({
  selector: 'app-file-upload-button',
  standalone: true,
  imports: [
    MatIconModule,
    ReactiveFormsModule,
    MatInputModule,
    MatButtonModule,
    MatFormFieldModule,
  ],
  templateUrl: './file-upload-button.component.html',
  styleUrl: './file-upload-button.component.css',
  providers: [
  {
    provide: MatFormFieldControl,
    useExisting: forwardRef(() => FileUploadButtonComponent)
  }
  ]
})
export class FileUploadButtonComponent {
  
  public fileName: string = '';
  public value: File | null = null;

  @Output() handleFile = new EventEmitter<File>();

  updateValue(event: any): void {
    const file: File = event?.target.files[0];
    if(file){
      this.fileName = file.name;
      this.value = file;
      this.handleFile.emit(file);
    }
  }

}
