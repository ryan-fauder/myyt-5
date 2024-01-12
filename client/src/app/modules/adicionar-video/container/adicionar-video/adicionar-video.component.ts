import { Component } from '@angular/core';
import { VideoPreviewComponent } from '../../components/video-preview/video-preview.component';
import { AdicionarVideoFormComponent } from '../../components/adicionar-video-form/adicionar-video-form.component';

@Component({
  selector: 'app-adicionar-video',
  standalone: true,
  imports: [
    VideoPreviewComponent,
    AdicionarVideoFormComponent
  ],
  templateUrl: './adicionar-video.component.html',
  styleUrl: './adicionar-video.component.css'
})
export class AdicionarVideoComponent {

}
