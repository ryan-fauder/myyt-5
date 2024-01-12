import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { FileUploadButtonComponent } from '../file-upload-button/file-upload-button.component';
import { VideoForm } from '../../../../interfaces/video';

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
    title: new FormControl<string | null>(null),
    file: new FormControl<File | null>(null),
    description: new FormControl<string | null>(null)
  })

  submitForm(event: any) {
    console.log(this.videoForm.value);
  }
  gravaArquivo(arquivo: any): void {
    const [ file ] = arquivo?.files;
    this.file = file;
    const reader = new FileReader();
    reader.onload = (event: any) => {
      this.preview = event.target.result;
    }
    reader.readAsDataURL(file);
  }
}
