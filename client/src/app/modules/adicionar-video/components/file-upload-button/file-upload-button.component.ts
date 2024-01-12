import { HttpClient, HttpEventType } from '@angular/common/http';
import { Component, Input } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { Subscription, finalize } from 'rxjs';

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
  styleUrl: './file-upload-button.component.css'
})
export class FileUploadButtonComponent {

  @Input()
  requiredFileType: string | null = null;

  fileName = '';
  uploadProgress: number | null = 0;
  uploadSub: Subscription | null = null;

  constructor(private _http: HttpClient) { }

  onFileSelected(event: any) {
    const file: File = event.target.files[0];

    if (file) {
      this.fileName = file.name;
      const formData = new FormData();
      formData.append("thumbnail", file);

      const upload$ = this._http.post("/api/thumbnail-upload", formData, {
        reportProgress: true,
        observe: 'events'
      })
        .pipe(
          finalize(() => this.reset())
        );

      this.uploadSub = upload$.subscribe(event => {
        if (event.type == HttpEventType.UploadProgress) {
          this.uploadProgress = Math.round(100 * (event.loaded / (event?.total ?? 1)));
        }
      })
    }
  }

  cancelUpload() {
    if(this.uploadSub){
      this.uploadSub.unsubscribe();
      this.reset();
    }
  }

  reset() {
    this.uploadProgress = null;
    this.uploadSub = null;
  }
}
