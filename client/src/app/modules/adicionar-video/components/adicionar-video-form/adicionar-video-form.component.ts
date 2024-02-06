import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { FileUploadButtonComponent } from '../file-upload-button/file-upload-button.component';
import { VideoForm } from '../../../../interfaces/video';
import { Subscription, finalize } from 'rxjs';
import { HttpClient, HttpEventType } from '@angular/common/http';
import { VideoService } from '../../../shared/services/video.service';

@Component({
  selector: 'app-adicionar-video-form',
  standalone: true,
  imports: [
    FileUploadButtonComponent,
    ReactiveFormsModule,
    MatButtonModule,
    MatIconModule,
    MatInputModule
  ],
  templateUrl: './adicionar-video-form.component.html',
  styleUrl: './adicionar-video-form.component.css'
})
export class AdicionarVideoFormComponent {
  public file!: File;
  public preview!: string;
  public videoForm = new FormGroup<VideoForm>({
    id: new FormControl<number | null>(null),
    title: new FormControl<string | null>(null, [Validators.required]),
    file: new FormControl<File | null>(null, [Validators.required]),
    description: new FormControl<string | null>(null, [Validators.required])
  })
  uploadProgress: number | null = 0;
  uploadSub: Subscription | null = null;

  constructor(private _videoService: VideoService) { }

  submitForm(event: any) {
    const formData = new FormData();
    formData.append("title", this.videoForm.value.title!);
    formData.append("description", this.videoForm.value.description!);
    formData.append("file", this.videoForm.value.file!);
    const upload$ = this._videoService.uploadVideo(formData)
      .pipe(
        finalize(() => this.reset())
      );
      this._videoService.getVideo(10).subscribe(
        video => {
          console.log(video);
        });

    this.uploadSub = upload$.subscribe(
      response => console.log(response)
    )
  }

  handleFile(file: any) {
    this.file = file;
    const reader = new FileReader();
    reader.onload = (event: any) => {
      this.preview = event.target.result;
    }
    reader.readAsDataURL(file);
    this.videoForm.patchValue({ file })
  }

  cancelUpload() {
    if (this.uploadSub) {
      this.uploadSub.unsubscribe();
      this.reset();
    }
  }

  reset() {
    this.uploadProgress = null;
    this.uploadSub = null;
  }
}
